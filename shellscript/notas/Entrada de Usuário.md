# Entrada de Usuário

Tags: #️⃣ Comandos

# read

Para receber uma entrada de usuário usamos o comando `read` se usarmos ele no terminal e depois digitar um nome, ele ira esperar a gente digitar algo e guardar esse valor dentro de uma variável com o nome digitamos na frente do terminal.

E possivel colocar varias variáveis, porem quando digitarmos eles ira colocar cara palavra separada por espaço em uma variável, e caso acha menos variáveis do que palavras a ultima variável fica com todo o resto

Nao esqueça que por ser um comando temos o `—help` para tirar duvidas

`-p` - Escolhemos um texto para ficar antes do que o usuario vai digitar para informar o que ele precisa digitar

`-s` - usado para senha por exemplo, onde o que digitar nao vai aparecer, igual quando usamos sudo e pedia a senha. 

# Usando Parâmetros

Parâmetros são opções que usamos depois de um comando por exemplo quando usamos `man ls` o ls esta sendo um parâmetro de man

Agora vamos usar parâmetros com script, vari veis que vão guardar o valor dos parâmetros

`$0` - Nome do Programa / Script

`$#` - Quantidade de Parâmetros

`$*` - Todos os Parâmetros inseridos

`$1-9` - Cada um dos parâmetros