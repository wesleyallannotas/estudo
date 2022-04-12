# Vetor

Tags: 🆓 Vetor

# Introdução

Maneira de otimizar a manipulação da memoria no que desrespeito a criação de variáveis. 

Estrutura de danos, Unidimensional(Uma fila de valores, uma dimensão), Homogênea(Todos os dados tem que ser do mesmo tipo) e Estática(Ele já ocupa a memoria quando e declarado o vetor, o contrario do dinâmico que só aloca o que esta usando).

É possível armazenar um conjunto de valores na memória do computador por meio do uso de vetores (Arrays, em inglês)

O vetor é a forma mais simples de organizarmos dados na memória do computador

Com vetores, os valores são armazenados na memória do computador em sequencia, um após o outro, e podemos livremente acessar qualquer calor do conjunto.

# **Vetor de Números**

Quando declaramos um vetor devemos informar o número máximo de elementos que poderá ser armazenado no espaço de memória que é reservado para o vetor.

Devemos também informar o tipo dos valores que serão armazenados no vetor

## **Sem Vetor**

Criamos uma variável para cada nota

![VetorExemSemVetor.png](Vetor%207da35/VetorExemSemVetor.png)

## **Com Vetor**

Criamos um vetor e navegamos por ele para usar os valor

Cada linguagem tem sua forma algumas utilizando o "0" outras começam a partir de "1", estudar a sua linguagem para saber.

![Vetorexemcomvetor.png](Vetor%207da35/Vetorexemcomvetor.png)

---

### **Exemplo**

Usamos uma estrutura "Para" para lançar os 10 valores dentro do vetor "n", de 0 a 9. (Estamos percorrendo índices dentro do vetor)

![VetorNumeroExemRepetçãoIncondicional.png](Vetor%207da35/VetorNumeroExemRepetoIncondicional.png)

### **Exemplo Vetor Numérico:**

Implemente um algoritmo que leia uma determinada quantidade de notas, informadas pelo usuário (Considere o limite máximo de 10 notas), calcule a medida das notas e imprima na tela.

![ExemploVetorNumerico.png](Vetor%207da35/ExemploVetorNumerico.png)

qtd = Igual a quantidade de notas que será digitada, pois mesmo o vetor sendo de 0 a 9, pode ser que use menos, por exemplo 5 notas.

Começamos a repetição para e informamos qtd-1 pois no pseudocódigo começa a contar a partir do 0 e não do 1.

# **Vetor de Caracteres.**

Uma variável literal pode guardar apenas um caractere ou um conjunto de caracteres, formando uma palavra ou uma frase.

Então, uma palavra ou uma frase podem ser interpretadas como uma sequência de caracteres, que também são chamadas de string.

Um string pode ser interpretado como um vetor de caracteres.

Para manipular uma strings, o computador precisa saber onde a sequência de caracteres termina.

Podemos guardar o tamanho da string, como fazemos com vetores em geral.

Ou podemos colocar uma marca no final da string, logo após o último caractere.

![VetorCaractere#1.png](Vetor%207da35/VetorCaractere1.png)

\o = Caractere Null para informar que terminou, e automático e as linguagens de programação fazem isso, logicamente cada uma de sua forma e com seu símbolo especifico.

Em vetor número usamos por exemplo uma estrutura "para" e pegamos valor por valor, já no caractere a linguagens ele sabe que cada caractere cairá em um espaço de memoria

### **Exemplo Vetor de Caracteres**

Implemente um algoritmo que leia um string e uma letra em duas variáveis distintas informadas pelo usuário (Considere o limite máximo de 11 letras para a string). Após isso, verifique se a string digitada contém a letra, caso positivo, informe quantas vezes esse evento ocorre.

![VetorCaractere#2.png](Vetor%207da35/VetorCaractere2.png)

Iniciamos ja atribuímos um valor zero ao i (que funciona como indice), para começar da primeira letra.

Enquanto não chegar no fim do vetor ou seja no Null ele ficara verificando se a letra daquele espeço de memoria e igual a letra que buscamos, caso nao seja passa pra frente, caso seja entra na estrutura "Se" e adiciona mais 1 a qtd, e para navegar pelo indice ele adiciona + 1 a ele.