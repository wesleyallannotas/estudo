# Formatando Texto no CSS

Created Time: January 22, 2022 12:50 PM
Tags: 📃 Texto, 🖌 CSS

## Comandos:

### Font:

**`font-family`** : Modificar a família da fonte `font-family:primeirafont, segundafont;` assim criamos uma prioridade de escolha de fonts ate achar a fonte que também tenha no computador do usuário.

**`font-size`** : Modificar o tamanho da fonte

**`medium` :** fonte do elemento com valor padrão de tamanho e equivalente ao padrão do browser. Os demais valores ( xx-small | x-small | small | large | x-large | xx-large) são calculados pelo browser considerando esse valor 'medium'.

**`larger | smaller` :** aumenta ou diminui o tamanho em relação ao valor herdado.

**tamanho  :** valor absoluto. Não são permitidos valores negativos.

**porcentagem :** porcentagem do tamanho do valor herdado

**`font-style`** : Estilo utilizado na fonte

**`normal` :** fonte do elemento sem efeito itálico ou oblíquo

**`italic` :** fonte do elemento com efeito itálico

**`oblique` :** fonte do elemento com efeito oblíquo

**`font-variant`** : Exibe o texto em pequena caixa-alta (versalete) ou fonte normal

**`normal` :** fonte do elemento sem efeito de capitalização 

**`small-caps` :** fonte do elemento com efeito de pequena caixa alta (versalete)

**`font-weight`** : Peso da fonte

**`normal` :** fonte do elemento com efeito padrão de peso (corresponde ao valor 400)

**`bold` :** fonte do elemento com efeito de negrito (corresponde ao valor 700)

**`bolder` :** fonte do elemento com o valor de peso imediatamente superior ao do valor herdado (p.ex: de 400 para 500)

**`lighter` :** fonte do elemento com o valor de peso imediatamente inferior ao do valor herdado (p.ex: de 400 para 300)

**font-color : NÃO EXISTE**

### Text

**`text-align`** : alinhamento do texto.

`left` : alinhamento do texto à esquerda

**`right` :** alinhamento do texto à direita

**`center` :** alinhamento do texto centralizado

**`justify` :** alinhamento do texto justificado

**`text-decoration`** : Atribui linhas no texto.

**`none` :** não produz decoração no texto do elemento

**`underline` :** cada linha de texto do elemento terá uma linha abaixo (sublinhado)

**`overline` :** cada linha de texto do elemento terá uma linha acima

**`line-through` :** cada linha de texto do elemento terá uma linha cortando-o ao meio (tachado)

**`blink` :** textos piscam-te alternadamente entre visíveis e não visíveis

**`text-indent`** : se tem espaçamento no começo do paragrafo ou não.

**tamanho :** valor absoluto. Não são permitidos valores negativos.

**porcentagem :** porcentagem do tamanho do valor herdado

**`text-tranform`** : se quer escrever tudo maiúsculo ou minúsculo.

**`capitalize` :** coloca o primeiro caracter de cada palavra do elemento em maiúsculas (caixa alta)

**`uppercase` :** coloca todos os caracteres de cada palavra do elemento em maiúsculas (caixa alta)

**`lowercase`** : coloca todos os caracteres de cada palavra do elemento em minúsculas (caixa baixa)

**`none` :** não aplica efeitos de capitalização

`text-shadow` : Basicamente colocar uma sombra no texto.

Temos 4 itens obrigatórios no `text-shadow`

text-shadow: 2px 2px 3px #FF0000;

text-shadow: (distancia para direita da sombra) (quanto abaixo vai a letra) (quanto esfumaçado será) (cor da sombra)

**`letter-spacing` :** Espaçamento entre caracteres

**`word-spacing`** : Espaçamento entre palavras

`line-height` : altura entre as linhas.

**text-color : NÃO EXISTE**

---

## Adicionando Fontes Externas

O site mais famoso para fontes é o google fonts

Seleciona a fonte e copia o link que ele dará e adiciona ao `<head>` depois adicionar esse fonte pelo CSS, puxando pelo nome da fonte.

Fonte externa se atribui entre aspas