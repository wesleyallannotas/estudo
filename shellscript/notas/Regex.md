# Regex

Tags: ⚙️ Regex

# Expressão Regular

Em toda nossa vida como programadores estaremos lidando com **regex** em algum momento, podemos aplicar o regex em qualquer sequencia de caracteres seja um paragrafo de um livro, um texto estruturado ou ate mesmo um conteúdo de um código

Com ela podemos lidar com as seguintes situações:

- Buscas
    
    Não e uma simples busca por palavras, podemos buscar por padrão que definem qual o formato do termo que estamos procurando, por exemplo procurar por datas com o padrão DD/MM/YYYY
    
- Substituição
    
    Vai muito alem de substituir texto por texto pois do regex podemos extrair uma parte do padrão para usar no destino, De: 2020-12-31 | Para: 31/12/2020
    
- Validações
    
    Verificar se uma determina sequencia de caracteres atende ao padrão estabelecido
    
     ❌01-01-2020 ✅ 01/01/2020
    

# Flags

Elas adicionam comportamentos adicionais a nossas regras, como:

`g` - indicar achar todas as ocorrências da regex

`i` - ignora **case sensitive**

case sensitive - quando ele é capaz de analisar uma cadeia de caracteres, avaliar a existência de caixa alta e caixa baixa e comportar-se de diferentes maneiras em função disso.

`m` - multilinha, lida com caracteres de inicio e fim `(^ e $)` ao operar em múltiplas linhas. 

# Operador pipe "`|`“

Algumas vezes precisamos dar match em mais de **um** termo, para isso usamos o operador pipe `|` . Ele funciona basicamente como nosso operador lógico **OR** `||`

# Conjuntos “[...]”

Com os conjuntos dizemos a regex que uma determinada casa pode ter diversos valores para dar match

> Tudo que eu digitar entre colchetes [..] em regex representa um carácter
> 

## Simples

Pre configuramos o conjunto, `[abc]` Esse ponto do regex aceita qualquer um entre abc.

## Range

Dentro dos nossos conjuntos. Podemos determinar um conjunto de match em letras que vão de **A** à **Z** ou pegue qualquer digito (**0** à **9)**, ****Um detalhe a ser observado é que o **range** obedece a mesma ordem da tabela **Unicode**, sendo assim regex como `[a-Z]` ou `[4-1]` produziram **erro**, pois ambas não estão na ordem correta da tabela Unicode, ou seja, o correto e `[A-Z]` ou `[a-z]` e o numérico `[1-9]`

Podemos também dar match em letras com **acentos** (é-à) ou (ç) usando

Temos também os **conjuntos negados**, que como o nome sugere, dar match em tudo que não faça parte do conjunto. Para definí-lo iniciamos a regra do conjunto com `^` , por exemplo `[^a-z]` que aceita tudo que não seja entre **a** à **z**. Vejamos um exemplo:

# Metacaracteres

Nas regex existem duas formas de caracteres, os **literais**, que representam o valor literal do caractere como `abc123` e os **metacaracteres** que possuem funções distintas dentro de um contexto na regex. Dois exemplos que acabamos de ver são o uso do `^` iniciando um conjunto negado e o uso do `-` em uma regra de conjunto com range`[1-9]` . Um metacaractere bastante recorrente é o **ponto** `.` , ele funciona como um **coringa**, sendo capaz de dar match em qualquer caractere

`.` - **Um** caractere qualquer  (espaço conta como carácter)

`\` - Uso de metacaracteres como **literal**

Necessário para forma literal de `^` e `-`

# Shorthands

Para simplificar a escrita e leitura das regex, possuímos algumas **shorthands** que são extremamente úteis para deixar ainda mais claro nosso código. Veja como podemos escrever esse conjunto `[0-9]` para `\d` ,`[a-zA-Z0-9_]` para `\w` ou para tratar espaços em branco `[\r\n\t\f\v ]` para `\s` simplificando ainda mais nossas regras

`\A` - Corresponde somente ao início de uma sequência.

`\b` - Corresponde a um limite de palavras, isto é, a posição entre uma palavra e um espaço.

`\B` - Corresponde a um limite.

`\d` -  Corresponde a um caractere de dígito.

`\D` - Corresponde a um caractere diferente de digito

`\f` - Corresponde a um caractere de alimentação de formulário.

`\n` - Corresponde a um caractere de nova linha.

`\r` - Corresponde a um caractere de retorno de linha.

`\s` - Corresponde a qualquer espaço em branco, incluindo espaços, tabulações, caracteres de alimentação de formulário, e assim por diante.

`\S` - Corresponde a qualquer caractere diferente de espaço em branco.

`\t` - Corresponde a um caractere de tabulação.

`\v` - Corresponde a um caractere de tabulação vertical.

`\w` - Corresponde a qualquer caractere de texto, incluindo sublinhado. Essa expressão é equivalente a [A-Za-z0-9_]

`\W` - Corresponde a qualquer caractere diferente de palavra. Essa expressão é equivalente a [^A-Za-z0-9_].

`\z` - Corresponde somente ao fim de uma sequência.

`\Z` - Corresponder somente ao fim de uma sequência ou antes de um caractere de nova linha no final.

# Quantificadores

Uma maneira de deixar suas regras ainda mais simples é com o uso dos quantificadores. Com eles podemos dizer quantas vezes uma **mesma** regra pode aparecer em **sequência**. relacionados com carácter anterior Vejamos elas:

`?` - zero ou um ocorrência, **Nenhuma ou uma vez**

`*` - zero ou mais ocorrências, **Nenhuma ou varias vezes**

`+` - uma ou mais ocorrências, **Uma ou mais vezes**

> Entre chaves {...} multiplica a expressão anterior
> 

`{n, m}` - de n até m

`{3}` - Tem que ter 3

`{1, 3}` - De um a 3

<aside>
💡 Pode se misturar metacaracter tipo . com um quantificador ficando `.*` por exemplo.

</aside>

# Âncoras

Muitas vezes vamos precisar **delimitar** a ação da nossa regex. Desse modo podemos usar três metas para nos auxiliar nessa função, Quando queremos tratar uma **palavra** que em suas extremidades não possua outra letra ou palavra, usamos a shorthands `\b`, Vale notar que caracteres com acentos ou `-` são considerados **bordas**.

`^` - inicio da linha

`$` - fim da linha

`\b` - inicio ou fim de palavra

# Grupos “(...)”

Os grupos que facilita ainda mais nossas regras. Eles nos possibilita a criação de regras isoladas, possibilita a criação de referencias (retrovisores) para o **reuso** da mesma regra em outro local dentro de uma mesmo regex e ainda cria a possibilidade de **validações** dentro da regex. Seu uso é muito **diverso**, dando **muito poder ao programador na hora de escrever suas regras**. Veja um exemplo:

```
pattern: /(\d{2})\/?(\d{2})?\/(\d{4})/
string:  Hoje é dia 20/01/2020
matches:            ^^^^^^^^^^
```

# Retrovisores

Uma função muito interessante dos grupos é que quando criamos algum grupo, este grupo é criando uma **referência**, que podemos acessa-lo em funções como o método replace (que vamos ver a frente) ou usar como **retrovisores** (mirror words) para fazer reuso de algum grupo que deu match anteriormente. Vejamos um exemplo baseado no exemplo anterior:

```
pattern: /\d{2}(\/?)\d{2}?\1\d{4}/g
string:  20/01/2020 25091991 25-09/2000
matches: ^^^^^^^^^^ ^^^^^^^^
```

No exemplo acima, veja que criamos o grupo `(\/?)` e para não repetí-lo em outro momento que necessitamos da mesma regra, usamos o retrovisor `\1` sendo `1` é ligado a **ordem** em que esse grupo foi criado. Podemos criar diversas referências para o reuso de regras.

Uma dica é se por exemplo usamos um grupo `(\w)` o seu retrovisor será o caractere que deu match com `\w`. Ex: \w = R seu \1 sera R.

# Grupos ignorados

Podemos definir grupos que podem ser **ignorados** (non-capturing groups) na hora do match usando a sintaxe `(?:)`. Vejamos um exemplo:

```
pattern: /([a-z]*)\s(?:ronaldo)/gi
string:  Cristiano Ronaldo
matches: ^^^^^^^^^^^^^^^^^
```

No exemplo acima, só foi **nomeado** um grupo, no caso *`([a-z]*)` pois o grupo `(?:ronaldo)` foi definido usando* `(?:)` e com isso não conseguimos manipulá-lo.

# Grupos aninhados

Com os grupos podemos criar grupos **aninhados** (grupos dentro de grupos). Vejamos um exemplo:

```
pattern: /((d[io])|(co))([a-z]{2})(do)/gi
string:  ditado colado dosado
matches: ^^^^^^ ^^^^^^ ^^^^^^
```

## Grupos especiais

Os grupos possuem **grupos especiais**. Como o **positive lookahead** `(?=)` e o seu oposto, **negative lookahead** `(?!)`. Com o positive lookahead podemos **verificar** se **existe** um grupo a frente de uma expressão ou grupo. Vejamos um exemplo:

```
pattern: /([a-z]+)(?=,)/gi
string:  Penso, logo existo
matches: ^^^^^
```

Falamos acima que a regex só dá match em palavras que à sua **frente**
 possuam virgula. Já o negative lookahead é exatamente o contrário do 
positive lookahed, ele pegará todos que não fazem parte do grupo 
especial. Vejamos um exemplo:

```
pattern: /([a-z]+)(?!,)\b/gi
string:  Penso, logo existo
matches:        ^^^^ ^^^^^^
```

Dentro dos grupos especiais ainda temos os **positive lookbehind** e **negative lookbehind**, porém como eles não possuem um bom suporte nos browsers decidi deixá-lo de fora deste post, porém pretendo abordá-los em post futuros.