# Comandos Linux

Tags: #️⃣ Comandos

Cada Usuário ganha um diretório próprio, esse diretório fica em /home seguido do seu username

Se tiver duvida sobre quem é você(seu username) basta perguntar ao linux com o comando no terminal.

`whoami` = Respondera falando o nome do usuário que esta utilizando no momento (caso aja mais de um usuário)

Para saber onde estamos ou seja o caminho usamos o comando `pwd` que vem de (p)rint (w)orking (d)irectory em português seria algo como imprimir o diretório corrente.

# Manual dos Comandos `man`

Usado para ver o manual do comando em linux, saber o que ele faz e quais opções ele aceita.

# Navegação por diretório `cd`

`cd` (c)hange (d)irectory

Todo diretório tem duas entradas padrão

. (Um ponto) = Representa diretório atual

.. (Dois pontos) = Representa diretório anterior

`cd` = Comando para navegar entre os diretórios

`cd $HOME` = Volta para nossa “casa”, ou seja, para o inicio.

`cd ~` = De forma mais curta volta para home

`cd /` = Voltamos para a raiz (root)

# Criar diretório `mkdir`

`mkdir` = vem de (m)a(k)e (dir)ectory

`mkdir` = Comando para criar um diretório.

# Comando para remover apagar `rm`

`rm` vem de (r)e(m)ove

`rm` = Comando usado para apagar.

# Comando para listar arquivos `ls`

Para ter uma listagem mais completa

`ls -l` = Listagem mais completa

`ls -la` = A diferença de apenas `ls -l` e que podemos ver os diretórios escondidos, que começão com . (ponto) que é o que determina se o diretório e escondido ou não.

# Criando arquivos com `touch`

E possível criar arquivos de diversas formas, porem a mais simples de criar um arquivo vazio e pelo comando `touch`

`touch` = Literalmente vai “Tocar” o arquivo se já existir um arquivo com esse nome ele alterar a data e hora da ultima modificação, se não existir ele vai criar um novo arquivo

# Comando para ver arquivos montados `df`

Com o comando `df` podemos verificar quais os dispositivos montados, com o uso do `-h` vamos ver com a divisão em 1024 (1gb)

Através desse comando caso inserimos um pendrive veremos que ele foi montado onde ele esta no sistema que estará ta coluna Filesystem, porem nesse caminho não conseguiremos usar comandos como o `cd` pois não existe um sistema de arquivos ali, so no ponto de montagem poderemos executar esses comandos, que se sera onde esta a coluna mounted on

# Comando para criar link simbólico

Um link simbólico nada mais é do que um atalho, por exemplo podemos ter um link simbólico dentro do nosso home que leva a um arquivo que se encontra dentro do nosso boot.

`ln -s arquivoorigem nomedolink`

Exemplo: `ls -s a.txt b.txt` = Criar um link do arquivo a.txt com o nome b.txt

# cat

Uso padrão imprime na tela o arquivo.

## Opções importantes

`-b` - numera as linhas que tem conteúdo (linhas em branco não)

`-n` - numera todas as linhas

`-A` - Mostra caracteres especiais, tabulação

# tac

Le o arquivo de baixo para cima.

# tail

Comando para ler o final do arquivo, por padrão le as ultimas dez linhas.

`tail -10` = para ler as ultimas 10 linhas

`tail -f` = Se prende ao final do arquivo, por exemplo podemos ficar verificando o que e adicionado no arquivo, ele atualiza em tempo real.

`-n` - Definimos o numero de linhas que ira ler.

# head

Mostra as primeiras linhas do arquivo

`-n` - Numero de linhas que ira mostrar

`-c` - Mostra os caracteres 

# wc

Conta os caracteres, palavras, linhas e bytes de um arquivo

[Linhas] [Palavras] [Caracteres] Ordem que aparece

# sort

Ordena os arquivos, em ordem alfabética por exempplo.

`-F` - Ordena ao contrario.

`-k` - Troca o indice de ordenacao

Por exemplo e um arquivos com nomes compostos como “Anderson SIlva” com `-k2` ira ordenar os sobrenomes.

`-t` - Informa o que delimita os campos caso ele nao entenda

Exemplo `-t”:”` informa que o que delimita os campos e o dois pontos.

`-g` - Ordena como numero (Por padrão ordena como string, ou seja, 0 1000 fica na frente do 114, por exemplo)

# uniq

Toda vez que ter algo repedido ele mostrara uma vez, por exemplo uma lista de nomes, se repetir os algum nome, usando esse comando, ele so ira aparecer uma vez.

`-u` - Mostra apenas o que apareceu uma vez

`-d` - Mostra apenas os que repetirao

`-c` - Exibira antes o numero de vezes que repeti-o depois o texto

Importante ordenar antes (comando sort)

# tr

Muda ou deleta caracteres dentro de uma string, e possivel mudar caracteres, especias, tabulação

Exemplo de Uso: (vindo de um pipe) `tr a e` muda toda letra a para e

`-d` - Deleta

# cut

Recorta pedaços de uma string

`-c` - caracteres

`(vem de um pipe) cut -c1-5` - vai mostrar apenas os 5 primeiros caracteres de cada linhas

`-c5-` - carácter 5 para frente

`-c-5` ate o carácter 5

`-c1,2,5` - Mostra o carácter 1 o 2 e o 5, exemplo nome antonio vai aparecer ann

`-c1,2,10-` - Mostra o carácter 1 e 2, e do 10 para frente

`-f` - campos

Pode ser usado a mesma logica do carácter para mostrar campos específicos

`-d` - Informa o que usaremos como o separador dos campos.

`-d” “` - O que sera interpretado como separador sera o espaço

Exemplo uma lista de nomes compostos (nome sobrenome) `cut -d” “ -f1` mostrara apenas o primeiro campo, ou seja, o primeiro nome.

# diff

Compara dois arquivos, seta vai indicar qual arquivo na ordem que colocamos, c e diferente, d diz que tem a mais.

`-w` - ignora espaço em branco como diferença

`-r` - Compara diretórios.

# grep

Busca padrão em arquivos.

Diferentes entre os grep

grep = expressão regular simples

egrep = expressão regular estendida

fgrep = apenas string nao aceita expressão regular

Procura um conteúdo dentro de uma string de texto

Exemplo de usp `grep cluadia nomes.txt` procura a string claudia no arquivo nome.txt

String completa, ou seja, Luiz Miguel, neste caso seria necessário o uso de aspas

Aceita uso de expressões regulares

`-i` - Tira a opção de case sensitive, ou seja, nao importa se e maiúsculo ou minusculo

`-c` - Conta quantas vezes achou aquele resultado

`-v` - Faz o inverso, ou seja, buscara o que nao corresponde ao colocamos

`-r` - entra e todos os diretórios e sub diretórios faz a busca 

`-l` - Lista, ou seja, nao mostra o resulta, so lista os arquivos que tem ele

`-A` - vem com a ideia de after, ou seja, `-A3` mostras 3 linhas depois do lugar onde encontrou o que buscávamos

`-B` - Mesma ideia que o de cima porem before, linhas antes

## Sintaxe do comando

`grep [OPÇÃO]... PADRÕES [ARQUIVO]...`

`Exemplo: grep -i "olá, mundo" text.txt`

### Diferença do comando egrep

egrep e simplesmente o grep com opção -E ativada por padrão

## Principais opções

Seleção e interpretação de padrão:

`-E, --extended-regexp` - PADRÕES são expressões regulares estendidas

`-F, --fixed-strings` - PADRÕES são textos
`-P, --perl-regexp`  - PADRÕES são expressões regulares Perl
`-f, --file=ARQUIVO`  - Obtém PADRÕES contidos no ARQUIVO
`-i, --ignore-case` - ignora diferenças entre maiúsculas/minúsculas nos padrões e dados
`--no-ignore-case`  - não ignora diferença de maiusculizações (padrão)
`-v, --invert-match` - seleciona somente linhas não coincidentes, ou seja, **inverte o comando**

### Exemplo

Exemplos do uso de `egrep` com expressão regular

`egrep “[Ll]inux” texto.txt` = Dentro do arquivo texto.txt lista todas srings Linux, que comece com l maiúsculo de minusculo

`egrep “b[eai]g” texto.txt` = Procurando uma string que comece com b, que tenha a letra ou a ou e ou i, e que termina com g

`egrep “b[a-o]g” texto.txt` = Procura strings que começa com carácter b, carácter a e o, carácter g.

`egrep “^Linux” texto.txt` = Pegas as strings que a primeira palavra e Linux 

e`egrep -v Linux texto.txt` = com o uso do `-v` não mostra os Linux e sim todo resto, -v inverte.

`egrep “Linux$” texto.txt` = Pegas as strings que a ultima palavra e Linux

`egrep -v “^$” texto.txt`  = Mostra tudo que não for linha em branco

`egrep “b[a-i]g*” texto.txt` = Mostra toda linha que tenha algo que inicie com carácter b, carácter entre a e i, carácter g que com `*`  pode não existir ou aparecer uma ou varias vezes.

`egrep “b[a-i]g+” texto.txt`  = Mostra toda linha que tenha algo que inicie com carácter b, carácter entre a e i, carácter g que com `+` tem que aparecer pelo menos uma vez

`egrep “b[a-i]g?” texto.txt` = Mostra toda linha que tenha algo que inicie com carácter b, carácter entre a e i, carácter g que com `?` tem que aparecer nenhuma ou apenas uma vez.

`egrep “O.Linux” texto.txt`  = Procurara caracter O, `.` esta informando que, queremos qualquer carácter(espaço e um carácter), depois o resto inux.

`egrep “O.*Linux” texto.txt` Procurara caracter O, `.` quais quer carácter(espaço e um carácter), 

`egrep “[Ll]inux\.” texto.txt` = Buscara a string Linux. e linux. pois com `\` antes do `.` ele perde a funca e passa a funcionar como um carácter.

# sed

O Sed é um editor de textos não interativo,do inglês (s)tream (e)(d)itor, ou seja, editor de fluxos (de texto).

## Sintaxe do comando

`sed [OPTION]... {script-only-if-no-other-script} [input-file]...`

Exemplo de uso : `sed -i ‘/[Ll]inux/d’ text.txt`

## Algumas opções

`-i` edita o arquivo original (faz backup se usado SUFIXO)

`-e` imprime na tela sem alterar o arquivo

`-n` faz a supressão, mostra só o resultado do comando

## Comandos em linha

`i\`  inseri texto

`s` substitui um trecho de texto por outro

`!` inverte a lógica do comando

`;` separador de comandos

`|` separador de strings

`d` no final deleta

`p` no final imprime

`g` no final (como se usa o d e p) altera todas as ocorrências, g de global.

`q` sai do sed , não continua o comando

## Exemplos

Exemplo de uso do sed com expressão regular

`sed -i 's/palavra/outra/' arquivo.txt` = troca todas as palavras em um arquivo por outra

`sed -n '9p' arquivo.txt` = Imprime só a nona linha

`sed -n '6,9p' arquivo.txt` = Imprime da sexta linha até a nona linha

`sed -i '/string/d' arquivo.txt` = Deleta todas as linhas que contém a palavra string no arquivo

`sed 's/^/palavra/' arquivo.txt` = Coloca uma palavra no inicio de cada linha

`sed 's/$/palavra/' arquivo.txt` = Coloca uma palavra no final de cada linha

`sed -n '/^http/p' arquivo.txt` = Imprime só as linhas que **começam** com a string ‘http’

`sed -i '/^http/d' arquivo.txt` = Deleta só as linhas que **começam** com a string ‘http’

`sed 's/marcos\|eric\|camila/pinguim/g' arquivo.txt` = Troca **todas** ocorrências da palavra “marcos”, “eric”, “camila” pela palavra “pinguim”

`sed 's/Marcos.*Eric/eles/' arquivo.txt` = troca tudo que estiver **entre** as palavras “Marcos” e “Eric” pela palavra “eles”

`sed -i '/^$/d' arquivo.txt` = Deleta linha em branco e altera o arquivo

`sed '/plop/s/foo/bar/g' arquivo.txt` = Substitui “foo” por “bar” somente as linhas que contém “plop”

`sed '/plop/!s/foo/bar/g' arquivo.txt` = Substitui “foo” por “bar” exceto as linhas que contém “plop”

`sed '2,7s/^/#/' arquivo.txt` = Insere da Linha 2 a linha 7 o “#” no início de cada linha

`sed -i '21,28s/^/NEW/' arquivo.txt` = insere a palavra ‘NEW’ no início de cada linha, da linha 21 até a linha 28

`sed 's/<[^>]*>/CODIGO/g' arquivo.txt` Troca tudo entre as tags “<” e “>” pela palavra “CODIGO”

`sed ':a;$!N;s/\n//;ta;' arquivo.tx`t = Coloca todas as linhas em uma só

`sed 's/.//' arquivo.txt` = Apaga o 1o caracter da frase

`sed 's/.//4' arquivo.txt` = Apaga o 4o caractere da frase

`sed 's/.\{4\}//' arquivo.txt` = Apaga os 4 primeiros caracteres

`sed -n '/^[[:digit:]]/p' arquivo.txt` = Imprime só linhas que começam com Números

## Formatando numero de telefone

Temos um arquivo com os números de telefone assim:

```
7184325689
4333285236
1140014004
3633554488
```

- O primeiro comando entre parênteses “\(..\)”
- Depois separado por barra \
- Lancei ou comando entre parênteses “\(.\{4\}\)”
- A saída do primeiro comando vai pro barra 1 “\1”
- E a do segundo comando pro barra 2 “\2”
- Poderia ter também o barra 3, n, …

Resultado ; `sed 's/\(..\)\(.\{4\}\)/(\1)\2-/g' arquivo.txt`

### sed para visualizar

Visualizar texto completo = `sed -n p nomearquivo`

Visualizar ultima linha = `sed '$!d' nomearquivo`

`$` = ao final

`!` = inverte o comando

`d` = deleta

Se tirar o `!` ele imprimira o testo todo sem a ultima linha.

## Criando loop no sed

Criamos um loop com `:nomedoloop`

Exemplo de loop:

`sed ':loop;$!N;s/\n /g;tloop' nomedoarquivo`

`:loop` - Criou o loop e deu o nome de loop

`$!N` - Ao final de cada linha antes de pular uma linha

`s/\n /g` - Linhas que pulam, virem espaço em branco

`tloop` - termina o loop

### Alterando // no arquivos para

No arquivo temos a string 

```
//usr/tpm/dir//path/
```

Para alterar no arquivos os trechos com // para 

`sed -i 's/\/\//\//g' nomearquivo`

`s` - substituir

`\/\/` = // (Lembrando que por barra ser um metacaractere precisa de escapa)

`\/` = 

`g` = global, ou seja, fazer a alteração no texto todo

**Como fazer sem precisar ficar escapando**

Pode fazer de forma mais simples sem precisar ficar escapando e poluir com muitas barras, mudando o operador de / para @.

O comando ficaria : `sed -i s@//@/@g' nomedoarquivo`

Pode ser usado o pipe também: `sed -i ‘s|//|/|g’ nomedoarquivo` 

# more e less

## more

Exibe o arquivos em paginas, Não muito recomendado para arquivos grandes pois ele lê tudo na memoria.

`Enter` - Desce uma linhas

`Espaço`- Próxima pagina.

`q` - Sai

## less

O mais recomendado porem, ele faz em streams, em vez de carregar tudo na memoria ele vai puxando tudo do stream, puxando o necessário para carregar uma tela, e ele permite usar alguns comados de navegação do vim.

Como no vi

`j` `k` - scroll pelo arquivos

`gg` - Ir para o topo

`G` - Ir para o fim

`/` -  Procura de cima para baixo

`n` - Próximo

`N` - Anterior 

`?` - Procura de baixo para cima

`n` e `N` em relação a que direção que procuramos, ou seja, ira fazer o movimento contrario.

`q` - Sai

# find

Procurar por arquivos e diretórios.

## Sintaxe

`find localbusca argumento`

`find ./ -name aluno.txt` 

`./` - Diretório atual

`-name` - Opção que informa que buscamos pelo nome.

`aluno.txt` - O que buscamos.

`aluno*` - Qualquer arquivo que comece com aluno

`*aluno*` - Qualquer arquivo que tenha aluno no meio

### Algumas Opções

`-type` - Atras dessa opção podemos por exemplo filtrar por diretórios `d` ou arquivos `f` entre outros

`-name` - Filtra por nome do arquivo, *.tgz (Qualquer arquivo com final .tgz) nomearq.* (Arquivos nomearq com qualquer extensão de final)

### Ideia interessante e misturar com o  `ls`

`find ./ -name alunos* -exec ls -l {} \;`

`find ./ -name alunos*` - Comando de busca

`exec ls -l {} \;` - Executa o ls -l em cada um dos resultados

`{}` - No lugar desse comando ele vai colocar o que encontrou no find

### Buscando arquivo modificado nos últimos 7 dias

`find /diretorio/caminho/ -mtime -7` - Encontra arquivos modificados nos últimos 7 dias

`find /diretorio/caminho/ -mtime +7` - Encontra arquivos modificados a mais de 7 dias.

<aside>
⚠️ Com o comando `find` podemos utilizar vários filtros, dês de por tipo de arquivo e nome do arquivo, usando o `-name` .tgz (O asterisco funciona como todos, ou qualquer coisa) ou nomearq.* Existem vários filtros no find que podemos brincar utilizando em conjunto.

</aside>

# date

Exibe a data como seu formato padrao, porem com opções podemos pedir especificamente o que queremos

`—help` - Mostra todas as opções de uso, como em todo comandoK

# seq

Gera um sequencia de numeros, `seq 10` cria uma sequencia de números de 1  a  10

Atribuindo um inicio `seq 5 10` o cria uma sequencia iniciando do 5 ao 10

Mudando quantidade que adicionara `seq 5 2 10` criara a sequencia de 5 a 10 adicionando 2 a cada linha em vez do padrão que e 1

# expr

Comando utilizado para fazer conta, sintaxe e com espaço, `expr 5 + 2` outra forma de fazer conta e usando o bc, a sintaxe ficaria `echo “(3+2)*5” | bc` seria 3 + 2 e dividir por 5