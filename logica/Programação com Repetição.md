# Programação com Repetição

Tags: ➿ Loop

- **Sumario**

# **Introdução**

Trata-se de uma forma de executar blocos de comandos somente sob determinadas condições, mas com a opção de repetir o mesmo bloco quantas vezes for necessário.

Cada vez que o conjunto de ações é repetida, acontece uma iteração.

As estruturas de repetição também são chamadas de laços, loopings ou loops. 

# **Laços, Looping ou loops**

Trate-se de uma estrutura de programação que facilita repetir determinados trechos de código.

Técnica utilizada para reduzir o trabalho de programação, principalmente quando é necessário repetir varias vezes alguma ação do programa.

## Os principais laços são

Incondicional ou contado. (for)

Condicional com teste no início (while)

Condicional com teste no fim

# **Repetição incondicional**

Quando é possível saber, de antemão, quantas vezes será necessário repetir uma ação, pode-se usar uma repetição incondicional ou  contada.

Pode ser um valor fixo, ou pode ser um valor informado pelo usuário, ou calculada pelo programa.

O valor sempre é conhecido antes de iniciar o laço.

![lacoincondionaloufor.png](Programac%CC%A7%2061a5e/lacoincondionaloufor.png)

**Caso omita o passo e sinal que ira subir de um em um.**

Exemplo 1:

Implemente um algoritmo que imprima os valores inteiros de 1 até 10.

![exemplacoincondicional.png](Programac%CC%A7%2061a5e/exemplacoincondicional.png)

---

Exemplo 2:

Implemente um algoritmo que leia as 3 notas e calcule a média.

**FORMA ANTIGA (Algoritmos sequenciais, antes de aprender sobre laço):** 

![exemploalacoincondicional2(formaantiga).png](Programac%CC%A7%2061a5e/exemploalacoincondicional2(formaantiga).png)

---

**FORMA DE RESOLVER COM O USO DE LAÇO:**

![A tabela a direita exibe em forma de tempo a alocação das variáveis na memoria.](Programac%CC%A7%2061a5e/exemplolacoincondicionalcorreto.png)

A tabela a direita exibe em forma de tempo a alocação das variáveis na memoria.

Primeiro declararemos as variáveis criando uma "i" para usar no laço, primeiro adicionamos 0 a memoria na variável soma, para limpa-la ou seja não correr risco de que recebe um valor aleatório que esta pela memoria, em seguida iniciamos o laço, onde colocamos que **para "i" de 1 (Atribui 1 a variável "i") ate 3 passo 1 faça, ou seja passaremos 3 vezes, adicionando mais 1 a variável "ï" ate o valor de 3 (dentro de "i") o laço se repetira, no 4 ele não repetira os comandos e ira para o fim para**, e enquanto estiver no laço, pedira para adicionar um valor de nota e ira adicionar esse valor ao montante da variável soma (Sobrepondo o valor anterior), depois que o laço se repetiu 3 vezes e foi para o fim para, iremos pegar o montante do valor guardado em soma e dividir por 3 (O mesmo numero de notas lançados, ou seja mesmo numero de loops) e jogar o valor da media para o usuário.

Precisa de uma variavel no caso "i" para ir guardando o valor que vai subindo para saber a hora de parar.

# **Comparação com a forma antiga**

Em comparação com a forma antiga ou seja o uso de algoritmos sequencias e agora com o uso de laço percebemos que  com o uso do laço só temos uma variável nota, e também possuímos uma **variável que funciona como acumulador (ou auxiliar)** que no caso foi a variável soma.

# **Otimizando algoritmo com laço incondicional do exemplo a cima:**

![orimizandoalgoritmolacoincondiconal.png](Programac%CC%A7%2061a5e/orimizandoalgoritmolacoincondiconal.png)

Com as alterações feitas no algoritmo da esquerda que resultou no algoritmo da direita, temos um algoritmo que não esta fixado a fazer uma media baseada em 3 notas, e sim um algoritmo que faz a repetição e calcula a media baseada no valor prévio digitado pelo usuário, ou seja, **guardando esse valor em uma variável que no caso é "qtd_notas" e a usando para fazer o numero de repetições e calcular a media.**

# **Repetição Condicional com Teste no Inicio**

Inicia a execução de um bloco de comandos quando uma condição é verdadeira.

Repete a execução desse bloco **enquanto a condição for verdadeira.**

Quando a condição **se torna falsa, execução do bloco é encerrada.**

![repetiçãocondicional.png](Programac%CC%A7%2061a5e/repetiocondicional.png)

---

**Exemplo 1:**

 (Usamos esse mesmo exemplo a cima porem no incondional, podemos usalo pois ja sabemos o numero de vezes, entre os dois metodos não tem diferença de performance, mas geralmente quando se sabe a quantidade de repetição se usa o incondional mesmo)

Implemente um algoritmo que leia 3 notas e calcule a média.

![A tabela a direita, simula o valor dentro da memoria com cada linha equivalendo a um passar do tempo.](Programac%CC%A7%2061a5e/exemplo1repetiocondicional.png)

A tabela a direita, simula o valor dentro da memoria com cada linha equivalendo a um passar do tempo.

**Explicando Variaveis:**

total = Primeiro zera para limpar a memoria depois serve como acumulador das notas.

cont = Primeiro zera para limpoar a memoria, depois serve como a variavel que ira delimitar o quanto de vezes sera reiniciado o laço.

nota = Serve como uma variavel auxiliar que em toda repetição guarda o valor que o usuario da para nota para poder somar com o montande ja guardado em "total".

---

**Exemplo 2:**

Implemente um algoritmo que leia a idade de varias pessoas e no final apresente a média das idades. o criterio da parada será a digitação de uma idade igual a zero ou negativa.

Observação:

Somente com a leitura do enunciado podemos perceber que precisaremos de um acumulador, que no caso sera o total para depois dividir pela media.

Tambem precisaremos de um contados, pois para haver a media precisaremos do total que estara no acumulador, e precisaremos saber quantas idades adicionamos no total, para isso o contador para fazer a conta total/contador

![exemplo2repetiçãocondicional.png](Programac%CC%A7%2061a5e/exemplo2repetiocondicional.png)

---

# **Repetição Condicional com Teste no Fim:**

Executa um cloco de comandos, independente da condição, somente então a condição é avaliada.

Caso ela seja verdadeira, então todo o bloco de sentença será executado novamente.

Este processo se repete ate que a condição seja falsa ai ela se encerra.

![RepetiçãoCondicionalTestFim.png](Programac%CC%A7%2061a5e/RepetioCondicionalTestFim.png)

---

**Exemplo:**

Implemente um algoritmo que leia 3 notas e calcule a média.

![exem1repetiçãoCondicionaltestfim.png](Programac%CC%A7%2061a5e/exem1repetioCondicionaltestfim.png)

Com o teste no fim a gente espera que sera execute pelo menos uma vez.

---

**Exemplo 2:**

implemente um algoritmo que leia a idade de varias pessoas e no final apresente a média das idades. o criterio da parada será a digitação de uma idade igual a zero ou negativa.

![exem2repetiçãocondiconaltestfim.png](Programac%CC%A7%2061a5e/exem2repetiocondiconaltestfim.png)

# **Comparação de Algoritmos e teste de funcionamente**

![exem2repetiçãocondiconaltestfim.png](Programac%CC%A7%2061a5e/exem2repetiocondiconaltestfim%201.png)

![exemplo2repetiçãocondicional.png](Programac%CC%A7%2061a5e/exemplo2repetiocondicional%201.png)

**Os dois algoritmos podem dar erro ⚠️**

## O primeiro

Pode dar erro caso a primeira idade adicionada seja negativa por exemplo (se a primeira idade for -5 e a segunda ser 20, passara pelo teste porem ira da errado o valor final) ou seja seria necessario uma estruta "IF" ou em pseudocodigo "se" para testes o primeiro, onde se fosse negativo ou igual a zero ele ja iria para um final onde apressenta o valor da media como zero, e nem passaria pelo laço.

## O segundo

Pode dar erro caso o valor da idade seja igual a zero ou negativa, pois ele iria direto paro o final do laço, onde daria erro pois a conta da media nao poderia ser executada, então para resolver seria necessario um "IF" ou em pseudocodigo "se" para caso desse falso e a idedade fosse negativa ou zero, ele em vez de executar a conta ja enviasse para o usario uma mensagem como a media sendo igual a zero.