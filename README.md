# Repositório PSET2 - LIGPROG

Este projeto realizado pelo aluno Lucas Zanon Guarnier da CC3M(2022/2) e foi orientado pelo professor [Abrantes Araujo Silva Filho](https://github.com/abrantesasf)  para a matéria de Linguagens de Programação.

---
**Questão 1:** Se você passar essa imagem pelo filtro de inversão, qual seria o output esperado? Justifique sua resposta.  
Output: (4, 1, [226, 166, 119, 55])  
Justificativa: 255 - c = pixel_invertido  
[255-29, 255-89, 255-136, 255-200] = [226, 166, 119, 55]  

---
**Questão 2:** Execute seu filtro de inversão na imagem imagens_teste/peixe.png, salve o resultado como uma imagem PNG e salve a imagem em seu repositório GitHub.  
Input:  
![bluegill](https://user-images.githubusercontent.com/89659834/188501033-b840c2ef-4de2-42fe-b22b-5a654e4ba6c9.png)  
Output:  
![peixe_invertido](https://user-images.githubusercontent.com/89659834/188334954-7ee3f4ac-3fb4-4897-aba7-344462517e6d.png)  

---
**Questão 3:** Considere uma etapa de correlacionar uma imagem com o seguinte kernel:  

![image](https://user-images.githubusercontent.com/89659834/188338472-3d1ada5d-f963-4632-a401-66998b5bec01.png)  

Qual será o valor do pixel na imagem de saída no local indicado pelo destaque vermelho?  
![image](https://user-images.githubusercontent.com/89659834/188335871-473a44f4-33ce-4895-a78f-309cc5803db7.png)  
 
 **Resultado:**  
0.00 x 80 = 0  
 -0,07 x 53 = -3, 71  
 0.00 x 99 = 0  
 -0.45 x 129 = -58.05  
 1.20 x 127 = 152.4  
 -0.25 x 148 = -37  
 0.00 x 175 = 0  
 -0.12 x 174 =  -20.88  
 0.00 x 193 = 0  
 0 + -3, 71 + 0 + -58.05 + 152.4 + -37 + 0 + -20.88 + 0 = 32.76  
 
---
**Questão 4:** Quando você tiver implementado seu código, tente executá-lo em imagens_teste/porco.png com o seguinte kernel 9 × 9:  
![image](https://user-images.githubusercontent.com/89659834/188336350-76612d2d-e63a-4fbd-8a99-663203fa6435.png)
  
**Input:**  
![pigbird](https://user-images.githubusercontent.com/89659834/188501144-d131b481-e6ae-4973-8ac7-21ce6163b58c.png)  
**Output:**  
![porcoq4](https://user-images.githubusercontent.com/89659834/188336391-461fa933-b424-4d9e-846f-b116c48704ff.png)  
  
---
**5.1 Desfoque:**  
Gerar a versão desfocada de gato.png  
**Input:**  
![cat](https://user-images.githubusercontent.com/89659834/188501203-08576da3-6241-41e7-87d3-77677dbd5f8c.png)  
**Output**:  
![catblurr](https://user-images.githubusercontent.com/89659834/188336785-37966cb8-3734-42c7-97fd-a2a086075297.png)  

---
**Questão 5:** se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação?  
Resultado: kernel = [[-1/9, -1/9, -1/9],[-1/9, 17/9, -1/9],[-1/9, -1/9, -1/9]]  
Justificativa: Seguindo a formula ![image](https://user-images.githubusercontent.com/89659834/188337930-22ccb721-ccd6-497c-b1b5-f3240e311e85.png) é possivel calcular o kernel acima com os seguintes passos:  
2 * I(x, y) é um kernel 3x3 composto apenas de 0 nas bordas e 2 no meio [[0, 0, 0], [0, 2, 0], [0, 0, 0]], assim dobrando o valor de cada pixel da imagem.  
B(x, y) é um kernel 3x3 com 1/9 em todas as posições [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]], serve para borrar a imagem
O kernel único para aumentar a nitidez da imagem então será um kernel 3x3 formado da subtração dos dois acima, resultando em um kernel formado de 0 - 1/9 (-1/9) nas bordas e 2 - 1/9 (17/9) no centro.  

**Input:**  
![python](https://user-images.githubusercontent.com/89659834/188501671-5f0d7ba6-c6a2-49f2-b960-de266a78ea3d.png)  
**Output:** Imagem gerada com a função sharpened (máscara de não nitidez):  
![pythonsharpened](https://user-images.githubusercontent.com/89659834/188338124-3ef86cab-b166-4c8d-9e4e-26c13a508fc4.png)  

---
**Questão 6:** Explique o que cada um dos kernels acima, por si só, está fazendo:  
![image](https://user-images.githubusercontent.com/89659834/188338346-416b34c5-ce06-4d5e-9cde-0fdcb88cecc9.png)  
O Kx retorna a detectação de bordas pela horizontal, enquanto o Ky retorna a detecção de bordas pela vertical  
Kx: ![ikx](https://user-images.githubusercontent.com/89659834/188338287-43c9d1df-62b0-4e37-9fda-1317952771e9.png)  
Ky: ![iky](https://user-images.githubusercontent.com/89659834/188338291-0c362bb1-435c-41b7-a306-7d215f196313.png)
  
**Input:**  
![construct](https://user-images.githubusercontent.com/89659834/188502171-49a59e81-be88-4f19-b53c-56854332e635.png)  
**Output:** Imagem obra após passar pelo filtro de bordas:  
![constructedges](https://user-images.githubusercontent.com/89659834/188338323-349465ac-c15b-443e-ab53-dc41580307c3.png)  
  
---  
