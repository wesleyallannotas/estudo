# Shebang e Execução do script

Tags: #️⃣ Shebang, ✅ Execução

# Shebang

Indicação de qual interpretador que deve ser utilizado nesse script 

`#!/bin/bash`

`#!` - **shebang** consiste de um cerquilha e um ponto de exclamação ("#!"), em seguida, seguidos pelo endereço (absoluto) para o interpretador.

# Executando o script

Podemos executar indicando o caminho do arquivo, indicando por extenso, ou caso esteja no diretório que estamos basta um `./` que indica diretório atual no terminal, desta forma ele executa em um shell filho e depois volta para o terminal atual com a resposta.

## Executando script no shell principal.

Para executar o shell em nosso terminal atual, ou seja, sem criar um shell filho para executar, usamos o comando `source` ou `.` 

## Executando com escolha do shell

Basta indicar antes em qual shell queremos executar, exemplo `bash script.sh`

# O que acontece se nao colocarmos o caminho

Por padrão ira procurar dentro da variável PATH os diretórios que ali estão, caso aja esse comando ele fara, caso nao acha vai dar erro, por isso o PATH e tao importante, ou seja, podemos adicionar a variável PATH o diretório que estão nossos scripts assim nao precisando indicar o caminho.

Lembrando que reiniciando o sistema iremos perder essa variável, mas caso deseje deixar esse diretório permanentemente ligado ao PATH basta editar o `~/.profile` adicionando a linha `PATH=”$PATH:~nomeusuario/caminhododiretorio”` ou seja, atribuímos que PATH recebe ele mesmo, para preservar os diretórios linkados já existentes, e depois adicionamos o novo diretorio.