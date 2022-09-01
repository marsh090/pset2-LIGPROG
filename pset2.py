from random import randint, random
import sys
import math
import base64
import tkinter

from io import BytesIO
from turtle import width
from PIL import Image as PILImage


class Image:
    def __init__(self, width, height, pixels):
        self.width = width
        self.height = height
        self.pixels = pixels

    def get_pixel(self, x, y):
        # Os seguintes if-else são o chamado efeito de borda, eles verificam se o kernel esta tentando pegar um pixel fora dos limites da imagem 
        # e devolvem um valor ao kernel para esses pixeis inexistentes
        if x < 0: # borda esquerda
            x = 0
        elif x >= self.width: # borda direita
            x = self.width - 1
        if y < 0: # borda em cima
            y = 0
        elif y >= self.height: # borda em baixo
            y = self.height - 1
        return self.pixels[(x + y * self.width)] # pixels[] pede o valor do indice do pixel na lista que forma a imagem, não as coordenadas do pixel.
                                                 # a formula x + y * self.width serve para calcular o indice do pixel sendo observado.
                                                 # Exemplo com uma imagem 11x11: 0 + 0 * 11 = 0
                                                 #                               1 + 0 * 11 = 1
                                                 #                                    ...
                                                 #                               10 + 0 * 11 = 10
                                                 #                               0 + 1 * 11 = 11

    def set_pixel(self, x, y, c):
        self.pixels[(x + y * self.width)] = c 

    def apply_per_pixel(self, func):
        result = Image.new(self.width, self.height)
        for x in range(result.width):
            for y in range(result.height):
                color = self.get_pixel(x, y)
                newcolor = func(color)
                result.set_pixel(x, y, newcolor) # x e y estavam invertidos e o result estava fora do for
        return result

    def correlacao(self, kernel):
        n = len(kernel) # variavel n criada pra guardar o valor do tamanho do array do kernel
        meio = n//2
        result = Image.new(self.width, self.height)
        for x in range(result.width):           
            for y in range(result.height):    # juntos os for x e for y verificam cada pixel da imagem
                newcolor = 0                  # newcolor (nome referente ao usado na função apply_per_pixel) guarda o valor gerado pelo kernel 
                for i in range(n):
                    for j in range(n):        # garante que a função passe por cada valor do kernel
                        newcolor += self.get_pixel((x-meio+j), (y-meio+i)) * kernel[i][j] # newcolor += usado pois o valor final do kernel aplicado a imagem é a soma de todos os valores do kernel x os pixeis da imagem
                result.set_pixel(x, y, newcolor)                                              # n//2 encontra o valor do raio do kernel
        result.acertar()                                                                      # x-/y- serve pra encontrar o pixel fora do centro que sera multiplicado pelo valor de mesma posição no kernel
        return result                                                                         # x-(n//2) e y-(n//2) serve para ver o primeiro pixel da imagem no kernel ((-1, -1) no caso de um kernel 3x3 no pixel (0, 0)
                                                                                              # +j/+i servem para, respectivamente, encontrar o pixel a direita/abaixo do primeiro
                                                                                              # x-(n//2)+j e y-(n//2)+i, kernel 3x3 no pixel (0, 0): 0-(3//2)+0 e 0-(3//2)+0 = (-1, -1)
                                                                                              #                                                    : 0-(3//2)+1 e 0-(3//2)+0 = (0, -1)
                                                                                              #                                                    : 0-(3//2)+2 e 0-(3//2)+0 = (1, -1)
                                                                                              #                                                    : 0-(3//2)+0 e 0-(3//2)+1 = (-1, 0)...
    def inverted(self):
        return self.apply_per_pixel(lambda c: 255-c)

    def blurred(self, n):
        raise NotImplementedError

    def sharpened(self, n):
        raise NotImplementedError

    def edges(self):
        raise NotImplementedError

    def darken(self):
        result = self.apply_per_pixel(lambda c: c * 0.5)
        result.acertar()
        return result

    def brighten(self):
        result = self.apply_per_pixel(lambda c: c * 2 + 1)
        result.acertar()
        return result

    # Função que garente que todos os pixeis da imagem gerada sejam inteiros entre 0  e 255
    def acertar(self):
        for x in range(self.width):
            for y in range(self.height):
                color = self.get_pixel(x, y)
                if color < 0: # Cor não pode ser negativa
                    color = 0
                elif color > 255: # Cor não pode ser maior que 255
                    color = 255
                color = int(round(color)) # Cor tem que ser um número inteiro
                self.set_pixel(x, y, color)

    # Below this point are utilities for loading, saving, and displaying
    # images, as well as for testing.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('height', 'width', 'pixels'))

    def __repr__(self):
        return "Image(%s, %s, %s)" % (self.width, self.height, self.pixels)

    @classmethod
    def load(cls, fname):
        """
        Loads an image from the given file and returns an instance of this
        class representing that image.  This also performs conversion to
        grayscale.

        Invoked as, for example:
           i = Image.load('test_images/cat.png')
        """
        with open(fname, 'rb') as img_handle:
            img = PILImage.open(img_handle)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299*p[0] + .587*p[1] + .114*p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Unsupported image mode: %r' % img.mode)
            w, h = img.size
            return cls(w, h, pixels)

    @classmethod
    def new(cls, width, height):
        """
        Creates a new blank image (all 0's) of the given height and width.

        Invoked as, for example:
            i = Image.new(640, 480)
        """
        return cls(width, height, [0 for i in range(width*height)])

    def save(self, fname, mode='PNG'):
        """
        Saves the given image to disk or to a file-like object.  If fname is
        given as a string, the file type will be inferred from the given name.
        If fname is given as a file-like object, the file type will be
        determined by the 'mode' parameter.
        """
        out = PILImage.new(mode='L', size=(self.width, self.height))
        out.putdata(self.pixels)
        if isinstance(fname, str):
            out.save(fname)
        else:
            out.save(fname, mode)
        out.close()

    def gif_data(self):
        """
        Returns a base 64 encoded string containing the given image as a GIF
        image.

        Utility function to make show_image a little cleaner.
        """
        buff = BytesIO()
        self.save(buff, mode='GIF')
        return base64.b64encode(buff.getvalue())

    def show(self):
        """
        Shows the given image in a new Tk window.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # if tk hasn't been properly initialized, don't try to do anything.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # highlightthickness=0 is a hack to prevent the window's own resizing
        # from triggering another resize event (infinite resize loop).  see
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        canvas = tkinter.Canvas(toplevel, height=self.height,
                                width=self.width, highlightthickness=0)
        canvas.pack()
        canvas.img = tkinter.PhotoImage(data=self.gif_data())
        canvas.create_image(0, 0, image=canvas.img, anchor=tkinter.NW)

        def on_resize(event):
            # handle resizing the image when the window is resized
            # the procedure is:
            #  * convert to a PIL image
            #  * resize that image
            #  * grab the base64-encoded GIF data from the resized image
            #  * put that in a tkinter label
            #  * show that image on the canvas
            new_img = PILImage.new(mode='L', size=(self.width, self.height))
            new_img.putdata(self.pixels)
            new_img = new_img.resize((event.width, event.height), PILImage.NEAREST)
            buff = BytesIO()
            new_img.save(buff, 'GIF')
            canvas.img = tkinter.PhotoImage(data=base64.b64encode(buff.getvalue()))
            canvas.configure(height=event.height, width=event.width)
            canvas.create_image(0, 0, image=canvas.img, anchor=tkinter.NW)
        # finally, bind that function so that it is called when the window is
        # resized.
        canvas.bind('<Configure>', on_resize)
        toplevel.bind('<Configure>', lambda e: canvas.configure(height=e.height, width=e.width))

        # when the window is closed, the program should stop
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()

    def reafter():
        tcl.after(500,reafter)
    tcl.after(500,reafter)
except:
    tk_root = None
WINDOWS_OPENED = False

if __name__ == '__main__':
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place for
    # generating images, etc.
    pass
    bordas = [[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]]
    borda2 = [[2, 1, 0],
              [1, 0,-1],
              [0,-1,-2]]
    Kx = [[-1, 0, 1],[-2, 0, 2],[-1, 0, 1],]
    Ky = [[-1, -2, -1],[0, 0, 0],[1, 2, 1],]
    Kxy = [[-2, -2, 0],[-2, 0, 2],[0, 2, 2],]
    borrar = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

    i = Image.load('test_images/cherry.png')
    b = i.correlacao(borrar)
    bb = b.correlacao(borrar)
    ikx = bb.correlacao(Kx)
    iky = bb.correlacao(Ky)
    ikxy = ikx.correlacao(Ky)
    ikyx = iky.correlacao(Kx)
    ikx.show()
    iky.show()
    ikxy.show()
    ikyx.show()

    # correla = i.correlacao(bordas)
    # i.show()
    # correla.show()

    # Kernel para resolver a questão 4
    # kernelq4 = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
    # i = Image.load('test_images/pigbird.png')
    # ic = i.correlacao(kernelq4)
    # ic.show()
    # i.show()
    
    


    # iv.save('test_results/peixe_invertido.png') salva a imagem peixe invertida

    # the following code will cause windows from Image.show to be displayed
    # properly, whether we're running interactively or not:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
