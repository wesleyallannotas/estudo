# Propriedade *Float*

Umas das propriedades que tem mais efeito colateral no mundo do *CSS*, usado bastante no passado para estruturar layout, **hoje em dia existe formas mais modernas**, se for necessário dar suporte e bom ter o conhecimento caso aja necessidade de manutenção em sites antigos, o objetivo inicial do float era deixar o que foi atribuído "flutuando"

Basicamente o float cria um novo contexto a frente do padrão, onde se encontra os elementos padrão do documento *HTML*.

## Fluxo Normal
*Divs* comuns sem aplicação de `float`

![CSS#12.png](Float%20e%20Clear/CSS12.png)

## `float:left`
Atribuindo a `div2` a propriedade `float` com o valor `left`, ela sai do fluxo normal criando um novo contexto a frente, a `div2` começara a "Flutuar", como consequência os outros elementos se reajustam, ou seja, a `div3` sobe ocupando o lugar antes da `div2`.

Porem como o comportamento do padrão do `float` e nao esconde conteúdo mesmo escondendo o elemento, então caso aja um texto por exemplo na `div3`, esse texto ficara a baixo  da `div2`.

![CSS#13.png](Float%20e%20Clear/CSS13.png)

## `float:right`
Agora se atribuirmos a div 3 o float right neste exemplo, a div vai sair da posição original e vai "flutuar a direita", e como não tenho nenhum elemento abaixo, não vai acontecer nenhum efeito colateral exceto com o container, pois eles mudam completamente seus elementos irmãos que estão do lado e no caso seu elemento pai, e como se fugisse e não reconhece mais de forma correta.

![CSS#14.png](Float%20e%20Clear/CSS14.png)

## Interação entre *Float*

**Elementos com float se entendem**, porem a `<div>` container para de encher aqueles elementos como filho para definir seu tamanho.

# Propriedade *Clear*

A propriedade `clear` funciona analisando de existe um elemento flutuando, ou seja, com a propriedade `float`, e caso aja ele limpara o contexto ficando embaixo do elementos flutuando.

Podemos atribuir 3 tipos de valores para `clear`, sendo eles `left`,`right` e `both` (Que significa ambos)

## `clear:left`

![CSS#15.png](Float%20e%20Clear/CSS15.png)

Atribuído a div 2 `float:left`, e atribuído a div 3 `clear:left`, o `clear` no div 3 faz com que a div 3 tente parar de encaixar na div 2 acima que possui o `float`, ou seja, ela ignora o comando que existe na 2

## `Clear:right`

![CSS#16.png](Float%20e%20Clear/CSS16.png)

## `clear:both`

![CSS#17.png](Float%20e%20Clear/CSS17.png)

Temos atribuído a div1 `float:left`, div2 ``float:right`, e div3 `clear:both`, ou seja, ele ignora qualquer `float` não importa se é left ou right ele será ignora por ele que.

# Elementos Reconhecer *Float*
Se dentro de um elementos possuir elementos com a propriedade `float` ou seja, "Flutuando", o nosso elemento pai nao reconhecera as dimensões desses elementos flutuantes, porem podemos corrigir isso usando a propriedade `overflow` atribuindo ao mesmo o valor `hidden`.  
Em código CSS:
```CSS
elementoPai {
    overflow: hidden;
}
```
A ideia de `overflow:hidden` e esconder qualquer elemento que vaze (overflow, alem do flow padrão) a altura ou a largura definida, ou seja, como nao definimos altura as dimensões ficam como *auto*, assim ele reconhecendo os elementos flutuando, ele decide exibir eles, assim alterando suas dimensões em vez de altera-los.

Assim se adicionarmos *height* ao elemento pai, ou seja, deixando de ser *auto*, ele vai esconder o que exceder desse tamanho nos elementos com `float`