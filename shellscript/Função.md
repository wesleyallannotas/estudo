# Função

Tags: 🛄 Função

# Introdução

Funções existem em todas linguagens de programacao, nada mais e do que um trecho de código, que atribuímos um nome a ele, e podemos chamar, e ele realizara aquele trecho

## Utilidade

- Evita a repetição excessiva de código
- Reduz o tamanho final do script
- Facilita a manutenção

## Características

Basicamente as funções são mini programas, no caso de script para entender mais fácil seria mina scripts que chamamos, ou seja, possui a mesma funcionalidade de qualquer script

- Pode Utilizar parâmetros
- Pode Utilizar variáveis globais ou locais
- Devem ser definidas antes de serem chamadas
- Podem ser utilizados códigos de torno

# Sintaxe

```bash
function nomefuncao () {
	Comandos
}

# E possivel omitir a palvra function

nomefuncao () {
	Comandos
}
```

# Chamando Funções

E como se estive utilizando um comando do shell, ou melhor executando um script no shell, então devemos ter atenção com o uso dos parâmetros

<aside>
💡 O que digitamos na frente do nome na função como part1 no exemplo a baixa, funciona como parâmetro dentro da função podemos ser chamado dentro da função por $1 $2 e dai por diante,

</aside>

```bash
# Forma 1
nomefuncao

# Forma 2
nomefuncao part1 part2

# Forma 3
VAR1=$(nomefuncao)`
```

# Variáveis com funções

- Global = Visível por todo o código (padrao)
- Local= Visível apenas na função

## Definindo variável local

Podemos definir uma variável como local apenas adicionando o local antes de atribuir a variável

`local VAR1="Shell Script"`

# Return Code

- Mesmo principio do Exit Code
- Definido pela instrução “return”
- Acessada por $?

## Exemplo

Usamos o `return 1`   e nao `exit 1` Pois o exit fecha o script, o return vai sair apenas da função

```bash
return 10
echo $?
# Retornara 10
```