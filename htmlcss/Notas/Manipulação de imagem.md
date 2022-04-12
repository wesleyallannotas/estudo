# Duas Formas para Inserirmos Imagens

### HTML

`<img src="..." alt="...">`

`<tag atributo="..." atributo="...">`

alt: texto alternativo caso não carregue sua imagem outra utilização e acessibilidade para deficientes visuais.

Podemos manipular o tamanho da imagem através de atributos por exemplo:  `width=""`(Largura) `height=""`(Altura), se adicionar apenas um atributo de tamanho o outro é atribuído proporcionalmente.

### CSS

background-image: url(..);

propriedade: valor(...);

## Quando usar HTML ou CSS

Conceitualmente HTML é conteúdo, CSS é visual, formatação, design.

Se a imagem possui carga informativa use HTML.

Se a imagem for decorativa, ou seja, apenas design visual use CSS.

Caso precise usar uma imagem em HTML para visual, insira o atributo alt porem deixe-o vazio.

## Tipos de Imagens

Formato Vetorial: Formado por vetor, Não perde resolução com Zoom.

Se sua imagem e jpg/jpeg tera que por a extensão no HTML.

**.jpg/.jpeg** : formato bitmap, compressão pesada perde um pouco de qualidade, Muitas informações de cores, Exemplo foto.

**.png** : formato bitmap, Utilizado com poucas cores, quando precisa de transparência(Mais suave).

**.gif** : formato bitmap, poucas cores, animação, também aceita transparência (porem e mais dura)

**.svg :** formato vetorial

**.webp :** formato bitmap, vantagem de ter tamanho de arquivo pequeno.

## Como usar CSS na imagem

Basta adicionar uma classe nela e depois lançar as motificações dentro do CSS

Exemplo (atribuindo class):

<img src="imagem" class="nomeclass" alt="descrição">

## Comandos Classe em CSS para imagem inserida pelo HTML

**float: left**

**float:** deixa flutuando 

**left**: direção