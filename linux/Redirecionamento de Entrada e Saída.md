# Redirecionamento de Entrada e Saída

Tags: #️⃣ Comandos

- **Sumario**

# Introdução

Todo comando recebe uma entrada conhecido como STDIN (0) normalmente o teclado passa pelo “programa” e tem duas saídas, saída do resultado SDTOUT (1) e saída de erro STDERR (2)

Temos como manipular mudando onde ira sair, de onde vai entrar.

# Redirecionando Saída

Saída e o resultado do nosso comando depois de passar pelo shell, o padrão e a tela

## Redirecionando resultado (SDTOUT) ”>” e “>>”

Com um comando de maior “>” ele cria um arquivo e coloca a saída dentro deste arquivo, se usarmos um arquivo já criado, ele sobrescreve o anterior.

Já se usarmos “>>” ira concatenar no final do arquivo, ou seja, adicionara o novo registro sem apagar o anterior.

## Redirecionando erro (STDERR) “2>” e “2>>”

Caso o comando de erro, se usarmos apenas o sinal de maior ele nao terá nada como saída, pois o comando deu uma mensagem de erro, e para redirecionar uma mensagem de erro e necessário o 2 antes do sinal de maior, como se sabe mensagem de erro e atribuído o 2, e o de resultado o 1 porem no comando de resultado omitimos o 1 usando apenas o sinal, a ideia de sinal de maior duplo e simples se aplica a mesma.

### Exemplos de uso

`cat aluno.txt > log.out` - Manda o resultado do comando para o arquivo log.out

`cat arquivoinexistente.txt 2> log-erro.out` - Erramos o arquivo, colocamos um inexistente, ou seja, ira gerar uma saída de erro, redirecionamos a saída de erro.

`cat arquivo.txt > log.out 2> log-erro.out` - Usando os dois comandos, ou seja, caso de certo redirecionamos para um arquivo, caso de erro, redirecionamos para outro

`cat arquivo.txt >> log.out 2>&1` - Dessa forma as duas saídas serão redirecionadas para o mesmo arquivo.

## Redirecionando Entrada

Por padrão e o teclado, alguns comandos como `tr` e muito usado o redirecionamento de entrada.

### “<” Redireciona Entrada

Ao contrario do resultado e erro, usamos agora o sinal de menor, por exemplo o comando `tr` necessita de redirecionamento seja por meio do “<” ou do pipe “|”

### Exemplo

`tr ‘a’ ‘Z’ < alunos.txt`