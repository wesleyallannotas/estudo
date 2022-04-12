# Instruções de Loop “for”, “while” e “untill”

Tags: 🔁 Loop

- **Sumário**

# Introdução

E utilizado para realizar uma serie de comandos ou instruções, mais de uma vez, criando um ciclo (loop), por exemplo utilizar uma serie de comandos para vários arquivos diferentes, ou uma serie de comandos ate que tao valor e alancado, entre outras formas de uso

<aside>
💡 Muito útil de usar no terminal fora do shell script também.

</aside>

# Loop com “for”

O “for” em Shell Script funcionado da forma em que cada interação que ocorro a sequencia de comando e executado e a variável recebe em sequencia os valores que colocamos apos o “in”

<aside>
⚠️ A sequencia de valores, podem ser simplesmente valor que escolhemos por exemplo `a,b,c` ou `1,2,3`, pode se usar File Globbing por exemplo `alunos*`, mas pode ser também comandos por exemplo `$(seq 5 10)`

</aside>

### Criando sequencia

Podemos criar sequencias de valor com o comando `seq` porem outra forma que a intrucao “for” aceita e entre chaves exemplo `{1..50..5}` neste caso sera criado uma sequencia ate o 50 com intervalos de 5 em 5, com o comando `seq` ficaria `$(seq 1 5 50)`

<aside>
⚠️ Importante perceber que entre `{..}` o que defini o intervalo vai no final, e no `seq` vai no meio.

</aside>

## Sintaxe

Sintaxe original pensada no shell script.

```bash
for variavel in valor1 valor2 ... valorN
do
	comando1
	comando2
	...
done
```

### Possível usar a sintaxe baseado no C

Com essa sintaxe conseguimos utilizar o uso mais comum do for nas linguagens de programacao, a formatação que vem dês da linguagem C.

<aside>
⚠️ Funciona no bash, pode ser que nao funcione no sh.

</aside>

```bash
# Valor inicial de i, depois ate onde vai
# E depois inforamos que ira incrimentar +1 por interacao.
for (( i=5 ; i <= 20 ; i++ ))
do
	echo "O numero e $i"
done
```

## “for” + IFS (Internal Field Separator)

Do português Separador interno de campos, Por padrão se utilizarmos um cat em um arquivo exemplo `for var in $(cat alunos.txt)` o loop fara uma interação com cada palavra do texto, pois o IFS padrão  são `“ “(Espaço) \t(Tab) \n(Quebra de Linha)`

### Redefinindo IFS

Começamos fazendo um backup do IFS padrão `OLDIFS=$IFS` 

Depois alteramos o IFS `IFS=novopadrao` exemplo `IFS=:`

Podemos atribuir mais de um separador, por exemplo do padrão são definidos 3 que são o espaço, quebra de linha e tab.

Voltando para IFS padrão `IFS=$OLDIFS`

<aside>
⚠️ IFS e utilizado pelo Shell, tomar cuidado quando utilizar, sempre volte para o padrão, uma ideia muito utilizada e criar um backup do IFS padrão e no final do script retornar ele.

</aside>

# Loop com “while”

While executa uma serie de comando enquanto algo for verdadeiro, enquanto uma condição for verdadeira, enquanto um comando retornar sucesso.

<aside>
💡 Muito útil de usar no terminal fora do shell script também.

</aside>

## Sintaxe

```bash
while <comando-condicao>
do
	Comando1
	Comando2
	...
done
```

# Loop com “until”

Semelhante ao while, porem enquanto o while faz a sequencia de comandos enquanto algo retorna como true ou seja verdadeira, o until realiza a sequencia de comandos enquanto for false ou seja falso, então ele ira realizar a sequencia de comandos e para quando retornar como verdadeiro. (Realiza a sequencia ate que seja verdadeiro)

## Sintaxe

```bash
until <comando-condicao>
do
	Comando1
	Comando2
	...
done
```

# Comando “continue” e “break”

Comandos que utilizamos nos nossos loop para funções extras, lembrando que apenas podem ser utilizados em loops

## break

`break` Utilizado para sair do loop, forcar que o loop seja interrompido.

<aside>
⚠️ Importante lembrar que ele sai do loop e nao do programa.

</aside>

### Sintaxe com exemplo:

```bash
while ls /var/lock/processo.lock > /dev/null
do
	if [ $(date +$H) -gt 18 ]
	then
		break
	fi
	echo "Processo em Execucao"
	sleep 30
done
```

## continue

`continue` Utilizado para voltar ao inicio do loop, ou seja impede que continue executando os comandos e volta para o inicio e vá para o próximo ciclo do loop

### Sintaxe com exemplo

```bash
while ls /var/lock/processo.lock > /dev/null
do
	if [ $(date +%H) -eq 18 ]
	then
		sleep 3600
		continue
	fi
	echo "Processo em Execucao"
	sleep 30
done
```