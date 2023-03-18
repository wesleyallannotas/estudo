# Instruções Condicionais “if” e “case”

Tags: 🔀 Condicionais

- **Sumário**

# Condicional “if” em shell script

A diferença do “if” padrão das linguagens de programação comum e do Shell e que no lugar da condição e colocado um comando, e o “if” ira verificar se o código foi executado com sucesso ou nao.

Sintaxe:

### Condição Simples

```bash
if <comando-condicao>
then
	comando1
	comando2
	comando3
fi
```

### Condição “else”

```bash
if <comando-condicao>
then
	comando1
else
	comando2
fi
```

### Condição “else if” (No shell se torna elif)

```bash
if <comando-condicao>
then
	comando1
elif <comando-condicao>
then
	comando2
else
	comando3
fi
```

# Condicional “case”

Case e usado quando temos varias valores dessa variável, e queremos dar uma resposta para cada valor pre definido, usado para nao ser necessário criar vários `else` dentro do `if` , ou seja, definimos quais os comandos que serão associados a cada padrão ou a cada valor de uma variável.

### Sintaxe

```bash
case $valor in
	padrao1)
		comandos
		;;
	padrao2)
		comandos
		;;
	*)
		comandos
		;;
esac
```

Sempre tem um variável, terminamos os comandos com 2 ponto e virgula “;;”

O padrão “*” e opcional, ele diz que caso nenhum dos padrões seja atingido cai neste.

## Case para menu

Dependendo do valor da variável opção, sera executado tal comando

```bash
case $opcao in
	1)
		echo "Opcao Incluir"
		;;
	2)
		echo "Opcao Remover"
		;;
	*)
		echo "Opcao Inexistente"
		;;
esac
```

## Case com expressão regular (Regex)

Executa uma das opções de código para determinado tipo de caracteres

```bash
case $caracter in
	[0-9])
			echo "O caracter informado e um numero"
			;;
	[A-Z])
			echo "O caracter informado e uma letra maiuscula"
			;;
	[a-z])
			echo "O caracter informado e uma letra minuscula"\
			;;
esac
```