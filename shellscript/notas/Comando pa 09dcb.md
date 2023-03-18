# Comando para fazer condição “test”

Tags: 🔀 Condicionais

- **Sumário**

# Comando para fazer condição

Lembrando que no if podemos usar um comando exemplo um grep, ou um condição que criamos por meio do comando `test`

`test` : Utilizado para criar um condição.

Existe vários outras opções para o comando `test` qualquer duvida usar `man test` no terminal.

Sintaxe: test <expressão>

## Testando Valores Numéricos:

`-eq` - Igual (equal))

`-ne` - Diferente (not equal)

`-gt` - Maior que (greater than)

`-ge` - Maior ou igual que (greater equal)

`-lt` - Menor que (lower than)

`-le` - Menor ou igual que (lower equal)

## Testando Strings:

`=` - Uma string igual a outra

`!=` - Uma string diferente da outra

`-n` - String nao nula

`-z` - String nula

## Testando Arquivos

`-f` - E um arquivo (testa se existe)

`-d` - E um diretório (testa se existe)

`-r` - Tem permissão de leitura

`-w` - Tem permissão de escrita

`-x` - Tem permissão de execução

`-s` - Possui tamanho maior que zero

# Outra forma se usar o test

Em vez de escrever o comando `test`, pode ser colocado o que vai ser testando entre colchetes `[..]`

Exemplo:

Usando comando:

```bash
VAR1=12

if test "$VAR1" -gt 10
then
	echo sucesso
fi
```

Usando colchetes:

```bash
VAR1=12

if ["$VAR1" -gt 10]
then
	echo sucesso
fi
```

# Carácter de negação “!”

O sinal de negação inverte o comando, ou seja, se o comando por padrão sairia como true com o sinal sera invertido para false.

```bash
VAR1=12

if [!"$VAR1" -gt 10]
then
	echo sucessoZ
fi
```

# “and” no comando `test`

O `-a` funciona como o “and” (.e.) 

```bash
VAR1=12

if ["$VAR1" -gt 10 -a "$VAR1" -lt 20]
then
	echo sucesso
fi
```

# “or” no comando `test`

O `-o` funciona como o “or”(.ou.)

```bash
VAR1=12

if ["$VAR1" -gt 10 -o "$VAR1" -eq 5]
then
	echo sucesso
fi
```

# Interação `-o` (or) `-a` (and)

Necessário tomar cuidado quando pretende usar os dois em uma mesma condicao pois o `-a` tem preferencia sobre o `-o` , ou seja, ira resolver primeiros os `-a` para depois ir para os `-o` para controlar essa execução como na matemática se usa os parenteses (..)

# Executando `test` no terminal

Quando executamos `test` no terminal não temos nenhum retorno, pois o resultado se deu certo ou não, fica armazenado no exit code, onde como foi aprendido com exit code, podemos consultar a ultima saída de código com a variável `$?`

# Exemplo de uso do “`if`”

Por padrão fara o "if" porem exibira o resultado do comando, então redirecionei a saída de sucesso do comando para a lixeira, Lembrando que usando "if" nao e necessário redirecionar a mensagem de erro também. como foi necessário no exercício de validação de usuário sem usar "if”

```bash
#!/bin/bash

if grep "$1" /etc/passwd > /dev/null 
then
  echo "Usuario Existente."
else
 echo "Usuario Inexistente."
fi
```

## Mesmo problema porem usando variável e o `test`

Com esse método nao e necessário redirecionar a saída do exit code, o comando sera executado dentro da variável e vamos analisar o resultado do comando, usando o `test`.

`-n` testa se a variável nao e nula.

```bash
#!/bin/bash

# Variaveis
USUARIO=$(grep "$1" /etc/passwd)

if test -n "$USUARIO"
then
    echo "O Usuario Existe"
else
    echo "O Usuario Nao Existe"
fi
```

## Toques finais para deixar mais profissional e clean

Omitir o comando `test` usando os colchetes [...]

```bash
#!/bin/bash

# Variaveis
USUARIO=$(grep "$1" /etc/passwd)

if [ -n "$USUARIO" ]
then
    echo "O Usuario Existe"
else
    echo "O Usuario Nao Existe"
fi
```

# Testar se o usuário digitou algum parâmetro.

Uma das formas de testar se o usuário digitou algum parâmetro e por meio do `$#` variável que guarda o valor da quantidade de parâmetros digitado, ou seja, se o valor for igual a 0 indica que o usuário nao digitou nenhum parâmetro

```bash
if [ "$#" -gt 0 ]

ou

if test "$#" -gt 0
```

Forma simples de testar, porem essa forma nao garante que o parâmetro digita esta correto.