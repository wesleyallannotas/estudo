# Programação com Decisão

Tags: ⁉️ Decisão, ➗ Operadores

# **Introdução**

As decisões **representam desvios** na execução do algoritmo

A decisão deve ser baseada em uma condição

Uma condição é uma **expressão booleana** cujo resultado é um valor logico **falso ou verdadeiro.**

Uma expressão booleana como condição é obtida por meio de uma **relação lógica entre dois elementos e um Operador relacional.**

Os elementos relacionados em um expressão lógica são representados por **relações binárias entre variáveis e constantes.**

# **Operadores**

## **Operadores Relacionais**

**Podemos comparar entre duas variáveis ou entre uma variável e um numero.**

![Operadores Relacionais.png](Programac%CC%A7%20cf19e/Operadores_Relacionais.png)

## **Operadores Lógicos**

![Operadoreslogicosconjuncao.png](Programac%CC%A7%20cf19e/Operadoreslogicosconjuncao.png)

Exemplo:

Condição 1: Dia ensolarado.

Condição 2: Ter meio de transporte

Resultado: ir à praia

Forma escrita: Amanha só vou para praia se estiver ensolarado **e** Ter uma carona.

**Ou seja usando o "e" é necessário que as duas condições sejam verdadeiras.**

![operaadoreslogicosdisjuncaoinclusiva.png](Programac%CC%A7%20cf19e/operaadoreslogicosdisjuncaoinclusiva.png)

---

Exemplo:

Condição 1: Ter carona.

Condição 2: Ter dinheiro para o taxi.

Resultado: ir ao cinema.

Forma escrita: Amanha para min ir ao cinema eu preciso ter uma carona **ou** ter dinheiro para o taxi

**Ou seja usando o "ou" é necessário que apenas uma condição seja verdadeira.**

# **Desvio Condicional**

## **Desvio Condicional Simples**

![desviocondicionalsimples.png](Programac%CC%A7%20cf19e/desviocondicionalsimples.png)

**Simples pois tem apenas um "se" não possui um "se não" por exemplo, ou seja se for verdadeira tem um comando se for falso, não, passa direto para o fim.**

### Exemplo:

![exemplodecisaosimples.png](Programac%CC%A7%20cf19e/exemplodecisaosimples.png)

## **Desvio Condicional Composto**

![desviocondicionalcomposto.png](Programac%CC%A7%20cf19e/desviocondicionalcomposto.png)

**Composto pois tem dois caminhos ou seja se for falso segui uma sequencia de instruções se for verdadeiro segui outra sequencia de instruções.**

### Exemplo:

![Desviocondicionalcompostoexem.png](Programac%CC%A7%20cf19e/Desviocondicionalcompostoexem.png)

---

### **Com duas condições:**

![desviocondcompostoduplo.png](Programac%CC%A7%20cf19e/desviocondcompostoduplo.png)

---

### Exemplo:

![desvioconndcompduploexem.png](Programac%CC%A7%20cf19e/desvioconndcompduploexem.png)

Testa primeiro a variável "x", seguia uma determina instrução para verdadeiro e outra determinada instrução para falso, depois o programa testa a variável "y", também possuindo um caminho de comandos para caso seja falso ou outro para caso seja verdadeiro.

### **Com uma condição dentro de outra condição:**

![condicaodentrocondicao.png](Programac%CC%A7%20cf19e/condicaodentrocondicao.png)

Exemplo 1: (Onde nota abaixo de 5 é E, nota abaixo de 9 e acima de 5 é B, e acima de 9 é A)

![exemcondidentrocondi.png](Programac%CC%A7%20cf19e/exemcondidentrocondi.png)

Exemplo 2: (Onde nota abaixo de 5 é E, nota abaixo de 9 e acima de 5 é B, e acima de 9 é A)

![disviodecondicaoexem2.png](Programac%CC%A7%20cf19e/disviodecondicaoexem2.png)

# **Problemas de Performance**

![problemaperformance.png](Programac%CC%A7%20cf19e/problemaperformance.png)

O algoritmo acima possui 3 condições simples, onde mesmo se o que procura esta na primeira menção ou seja a nota e 9,5, ele ainda passara pelos outros testes, ou seja, funciona para o que precisa porem perdendo tempo consequentemente performance.

**Solução:**

![problemaperformace2.png](Programac%CC%A7%20cf19e/problemaperformace2.png)

Usando a condição composta, com uma menção dentro da outra ganhamos mais performance, e economia de tempo.

# **Decisão por seleção**

**Algumas linguagens de programação não implementa, já outras denominam de forma diferente.**

![dcisaoseleção.png](Programac%CC%A7%20cf19e/dcisaoseleo.png)

No algoritmo a cima ira digitar o numero correspondente ao dia e o algoritmo ira fazer os testes ate chegar em um que bata e saia a resposta do dia da semana correspondente.