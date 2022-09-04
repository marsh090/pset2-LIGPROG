# Repositório PSET2 - LIGPROG

Este projeto realizado pelo aluno Lucas Zanon Guarnier da CC3M(2022/2) e foi orientado pelo professor [Abrantes Araujo Silva Filho](https://github.com/abrantesasf)  para a matéria de Linguagens de Programação.

---
**Questão 1:** Se você passar essa imagem pelo filtro de inversão, qual seria o output esperado? Justifique sua resposta.  
Output: (4, 1, [226, 166, 119, 55])  
Justificativa: 255 - c = pixel_invertido  
[255-29, 255-89, 255-136, 255-200] = [226, 166, 119, 55]  

---
**Questão 2:** Execute seu filtro de inversão na imagem imagens_teste/peixe.png, salve o resultado como uma imagem PNG e salve a imagem em seu repositório GitHub.  
Output:  
![peixe_invertido](https://user-images.githubusercontent.com/89659834/188334954-7ee3f4ac-3fb4-4897-aba7-344462517e6d.png)  
Codigo:  
![function_inverted](https://user-images.githubusercontent.com/89659834/188334752-000f5f7b-3967-46f4-abab-81b7fb683789.png)  
![question_2](https://user-images.githubusercontent.com/89659834/188334938-b724e838-7be6-494c-aeca-29607a93095b.png)  

---
**Questão 3:** Considere uma etapa de correlacionar uma imagem com o seguinte kernel:  

||||
|--|--|--|
|0.00|-0.07|0.00|
|-0.45|1.20|-0.25|
|0.00|-0.12|0.00|  

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
  
**Resultado:**  
![porcoq4](https://user-images.githubusercontent.com/89659834/188336391-461fa933-b424-4d9e-846f-b116c48704ff.png)
  
---
**5.1 Desfoque:**  
Gerar a versão desfocada de gato.png
Resultado:  
![catblurr](https://user-images.githubusercontent.com/89659834/188336785-37966cb8-3734-42c7-97fd-a2a086075297.png)

---
**Questão 5:** se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação?  
