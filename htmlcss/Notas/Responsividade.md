# Responsividade

Created Time: January 22, 2022 12:50 PM
Tags: 📲 Responsividade, 🖌 CSS, 🧬 HTML

# Mobile First

Traduzindo diretamente seria celular(dispositivo móvel) primeiro, primeira desenha para mobile depois adapta para computador, porem normalmente quando é desenhado para mobile e depois e aberto em computador fica um site muito simplista para desktop.

Com a evolução desse pensamento, hoje se pensa que, tem que desenhar o site para maior tela possível, já pensando em como adaptar para a menor possível.

# Layout Normal(básico) x Layout adaptativo x Layout responsivo

### Layout Normal(básico)

Não possui responsividade alguma, é projetado para desktop e ponto, o site não se adapta a telas menores, mantem seu tamanho.

### Layout Responsivo

Pensado para diminuir ou aumentar de tamanho de acordo com o tamanho da tela do usuário, ou seja, o layout responde ao tamanho da tela.

### Layout Adaptativo

Ele adapta ao tamanho da tela especifica, não é de forma fluida como o responsivo, ou seja, ele possui tamanhos específicos para se adaptar, não vai se flexibilizar pra qualquer tamanho de tela, e sim tem seus tamanhos de tela padrão já programados para se adaptar.

### Qual utilizar

Dependendo do site será necessário apenas o responsivo, porem na maioria da site será um mix de adaptativo com responsivo, por exemplo vai diminuindo de forma responsiva o site, porem chega em um ponto que não cabe a mesma estrutura, então ele se adapta a uma nova estrutura e continua diminuindo de forma responsiva.

Normalmente se adapta nos tamanhos(width) : 320(celular comun), 480(celular grande), 760(tablet), 960(monitor menor), 1200(monitor hd), 1600(monitor full-hd). 

Pode fazer com menos resoluções para se adaptar por exemplo, faça com 960 podem ser responsivo para mais, assim diminuí para 3 versões, 320, 760, 960 (Celular, Tablet, Desktop)

# Adicionando Viewport na meta tag (HTML)

Tag meta : `<meta name="viewport" content="width=device-width, user-scalable=no">`

Explicando :

Dentro do conteúdo do nosso viewport(como o navegador vai interpretar as dimensões de navegação da pagina)

`width=device-width` A largura será igual a largura do device(celular, table, desktop) do usuário

`user-scalable=no` Isso quer dizer que o usuário não poderá dar zoom

`initial-scale=1.0` Define a escala inicial do site quando aberto, assim possibilitando zoom.

`minimum-scale` Controla a escala mínimo de onde o usuário pode tirar o zoom.

`maximum-scale` Controla a escala máxima de zoom que o usuário pode dar

# Imagens Responsivas

Importante : `background-size` funciona em imagens inseridas como background, o `object-fit` funciona em imagens de verdade, como a tag img.

## Picture e Source (HTML)

A imagem não mudara de tamanho, e sim quer dizer que mudaremos a image de acordo com a resolução que a gente quer.

Usaremos as tags `<picture>` e `<source/>`

Dentro de `<picture>` colocaremos nossa imagem

```html
<picture>
	<img src="imagens/Code.png" alt=""/>
</picture>
```

Agora adicionando a tag `<source/>` para que quando a tela mude de tamanho mude a imagem.

`<source/>` tag que fecha nela mesma então adicionaremos atributor

`media=""` Condições para que a foto que colocamos em `srcset=""` seja escolhida.

`(min-width: )` A partir desse tamanho vai usar essa foto, o mínimo de tamanho para que essa imagem funcione (Deste tamanho para cima)

`(max-width: )` Tamanho máximo que a imagem ira funcionar (Deste Tamanho para Baixo)

`srcset=""` Link a nova imagem a ser exibida. 

```html
<picture>
   <source media="(min-width: 600px)" srcset="imagens/121537.png"/>
   <source media="(min-width: 510px)" srcset="imagens/g-1.jpg"/>
   <img src="imagens/Code.png" alt=""/>
</picture>
```

## Propriedade object-fit (CSS)

Se adicionarmos as propriedades width e height em uma imagem normalmente ira apenas distorcer para alcançar aquele tamanho, se adicionarmos apenas width(largura) o height(altura) será auto(automático) então manteria a proporcionalidade e vice versa caso atribuirmos apenas height(altura), porem via CSS podemos manter as propriedades de width e height que queremos corrigindo essa distorção, atraves da propriedade `object-fit` 

`object-fit` : Propriedade usada para controlar a distorção da imagem.

`fill` : Utilizado como padrão, basicamente a imagem será redimensionada independente da proporção, de forma a caber e mostrar ela inteira na área disponível, ou seja, se precisar distorcer ira fazer.

`contain` : Diminui a imagem mantendo a proporção, de forma que a imagem inteira consiga aparecer no espaço disponível, sem distorcer, o espaço que não foi possível colocar nada, não terá nada, pois ele não duplica a imagem nem a distorce, então fica um espaço vazio, transparente.

`cover` : Um dos mais utilizados, ira manter a proporção da imagem, mas vai cortar a imagem, afim de dela preencher todo o espaço disponível, primeiro ele diminui ou aumenta a imagem para caber no seu espaço disponível, e o que sobrar para não distorcer ele corta sempre e relação ao meio para manter o centro da imagem

`none` : Mantem a imagem no tamanho original, e corta em relação ao centro, a maior diferença entre `none` e `cover` e que no cover a imagem e redimensionada de depois cortada, ja no `cover` se mantem o tamanho original e apenas corta.

`scale-down` : Muito pouco usada, bem similar ao `contain`, a diferença é que diminui proporcionalmente a qualidade bem como o tamanho, para caber no nosso tamanho especificado, em `contain` mantem a qualidade.

# @media (CSS)

Mais vai utilizar em relação a responsividade, dará o inicio para o site ficar responsiva

Quando as condições de `@media` forem satisfeitas, ele executara aqueles código de CSS para substituir códigos anteriores ou adicionar código.

Exemplo mudando `background-color` :

```css
body {
    background-color: #000;
}

@media (max-width: 600px) {
    body{
        background-color: #f00;
    }
}
```

Quando o tamanho máximo de width(largura) for 600px, ou seja, de 600px para baixo, a cor do background sera vermelha(#f00)

## Trabalhando com mais de uma condição de @media

E necessário fazer de uma forma que uma não sobrescreva a outra.

### Com 3 condições diferentes :

Trabalharemos com uma `@media` usando max-width, ou seja, desse tamanho determinado para baixo, vale o que tem dentro de media, outro `@media` usando min-width, ou seja, desse tamanho para cima seguira as propriedades colocados dentre dessa outra `@media`, e o terceiro será o nosso CSS normal sem o uso de media, que ficara nesse intervalo de valor entre os dois

Exemplo:

```css
body {
    background-color: #0f0;
}
@media (min-width: 1000px) {
    body {
        background-color: #00f;
    }
}

@media (max-width: 600px) {
    body{
        background-color: #f00;
    }
    h1  {
        font-size: 15px;
    }
}
```

Com 1000px de width(largura) para cima vale as propriedades dentro da primeira `@media` , se a largura for menor que 600px valera as propriedades dentro da segunda `@media` , e entre os valores de 600px e 1000px valera o que tiver no nosso CSS normal, ou seja fora das `@media`.

### Com quatro condições ou mais :

A partir de quatro condições, será necessário o uso do `and` para criar uma estensão no funcionamento naquela `@media` usando o min-width e o max-width.

Exemplo:

```css
body {
    background-color: #0f0;
}
@media (min-width: 1000px) {
    body {
        background-color: #00f;
    }
}

@media (min-width: 700px) and (max-width: 1000px) {
    body {
        background-color: purple;
    }
}

@media (max-width: 400px) {
    body{
        background-color: #f00;
    }
    h1  {
        font-size: 15px;
    }
}
```

Acima de 1000px de width vale a primeira `@media`, entre 700px a 1000px vale a segunda media, entre 400px a 700px vale o nosso CSS normal sem o uso das `@media`, e de 400px para baixo vale a ultima `@media`.

### Outra ideia com quatro condições :

```css
body {
    background-color: #0f0;
}
@media (min-width: 1000px) {
    body {
        background-color: #00f;
    }
}

@media (min-width: 700px) and (max-width: 1000px) {
    body {
        background-color: purple;
    }
}

@media (min-width: 300px) and (max-width: 700px) {
    body{
        background-color: #f00;
    }
    h1  {
        font-size: 15px;
    }
}
```

Dessa forma nosso CSS patrão será o abaixo de 300px.

## Alguns outros usos do @media

Através do `@media only print {}` Criamos um media que só ira parecer suas propriedades quando o usuário for imprimir, ou seja, usando "crtl + p", muito utilizado para remover coisas da tela quando for imprimir, por exemplo para imprimir boletos.

Dica: Usando `display: none;` o que queremos ocultar some.

`@media only screen {}` Através desse @media só ira aparecer na tela, e quando for imprimir não, outra forma de utilizar. ou seja, o inverso.

`@media all {}` Aplica para todas condições.

## Orientation no @media

Basicamente serve para detectar se a tela esta majoritariamente horizontal ou vertical, e assim podem alterar dependendo de qual orientação se encontra

`@media (orientation: landscape) {}` : Identifica como orientação majoritariamente horizontal

`@media (orientation: portrait) {}` : Identifica como orientação majoritariamente vertical

### Exemplo do uso:

HTML da Pagina:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsividade</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <div>Caixa 1</div>
    <div>Caixa 2</div>
    <div>Caixa 3</div>
    <div>Caixa 4</div>
</body>
</html>
```

CSS da Pagina:

```css
body {
    display: flex;
}
div {
    width: 100px;
    height: 100px;
    border: 3px solid black;
}
@media (orientation: landscape) {
    body {
        flex-direction: row;
    }
}
@media (orientation: portrait) {
    body{
        flex-direction: column;
    }
}
```

Dessa forma quando a tela tiver horizontal ira jogar as divs uma do lado da outra, e quando tiver vertical ira posicionar as divs uma abaixo da outra, isso e apenas uma ideia, usando essa ideia de `@media` mudamos mudar o que quisermos, tirar coisas colocar coisas mudar cor, nossa imaginação e o limite.

### Dica Importante para o uso de orientaion

Ele não trabalha com a posição real do celular, ou seja, ele não detecta a posição que o celular se encontra na sua mão, e sim detecta a proporção de tela, verificando se width ou height e maior.

Exemplo e dependendo do tamanho da tela do celular, caso abra o teclado, ele pode mudar qual e predominante entre width e height, assim podem mudar a orientaion do `@media`.

## Aspect-ratio no @media

Técnica pouca utilizada, pois tem utilidade em casos bem específicos, iremos usar os valores de aspect-ratio conhecidos como o de 16/9, 4/3, ou seja, comparando as proporções entre width e height, seguindo a logica o `aspect-ratio 1/1` seria um quadrado perfeito.

`@media (aspect-ratio: 1/1) {}` 

Podemos também utilizar do min e do max para aspect-ratio, 

`@media (min-aspect-ratio: 1/1) {}`

`@media (max-aspect-ratio: 1/1) {}` 

Normalmente se utilizada com o min ou max, mas sem eles, fica muito especifico a apenas aquele aspect-ratio perfeito.

# Função var (CSS)

Utilizando variáveis no CSS, como? e para que usar?, as variáveis vem para resolver os problemas como por exemplo ter que alterar uma cor em vários lugares, em vez disso, possuindo uma variável com aquela cor e só alterar a variável. Quando crio uma variável no CSS, ela só funciona no elemento onde foi criado ou nos elementos que estiverem dentro dele, uma forma para criar e deixar disponível para todo documento e utilizando `:root` , porem se quisermos criar uma variável dentro de uma div para utilizada nela e em seus filhos, não tem problema algum, porem geralmente se cria todos no `:root`

Tirando a duvida do por que não utilizar `* {}` ou `:root` ou `html {}`

`* {}` : Todo mundo, as propriedades definidas dentro de asteriscos no css será injetada/ fará efeito em todos os elementos; tags do html, Ex: body, div, span, p, a,,
`:root` : elemento raiz de um documento, mas como a gente sempre usa com HTML ele equivale a tag html
`html {}`: As propriedades adicionadas aqui, irão ter efeito na tag <html> do documento, também pode adicionar variáveis globais

## Como criar uma variável no CSS

Se inicia com 2 traços, depois coloca o nome da variável.

Exemplo: `—bg-color: #000;` Criei uma variável com o nome bg-color guardando como informação a cor preta.

## Como chamar a variável no CSS

Colocamos `var(nomedavarivel)` , ou seja, utilizamos o var e dentro dos parênteses colocamos o nome da variável que criamos anteriormente.

### Exemplo de uso das variáveis no CSS:

```css
:root {
    --bg-color: #000;
    --bg-second: #444;
    --font-color: #fff;
}

body {
    background-color: var(--bg-color);
}
h1 {
    color: var(--font-color);
}
.container {
    background-color: var(--bg-second);
    color: var(--font-color);
}
```

### Como usar uma var porem caso ela não exista, substituir por um valor especifico.

Basicamente colocaremos uma virgula na frente do nome da variável e adicionaremos a alternativa.

Exemplo: 

```css
h1 {
    color: var(--font-color, #00f);
}
```

Caso não encontre a variável, ira para o que tiver após a virgula, podemos invés de colocar um valor especifico atribuir outra variável depois da virgula.

## Função var em media query

Alguns erros com o uso de var, funciona porem não e a forma correta de se usar as variáveis, e depois a forma correta.

### [Errado] Usar variável no começo depois no fim não:

```css
:root {
    --bg-color: #fff;
    --bg-second: #ccc;
    --font-size: 25px;
}

body {
    background-color: var(--bg-color);
    font-size: var(--font-size);
}
h1 {
    color: var(--font-color, #00f);
}
.container {
    background-color: var(--bg-second);
    color: var(--font-color);
}

@media (max-width: 450px) {
    body {
        font-size: 14px;
    }
}
```

### [Errado] Criar varias variáveis com nomes diferentes:

Cria mais de uma variável com nome diferente para fazer uma mesma função.

```css
:root {
    --bg-color: #fff;
    --bg-second: #ccc;
    --font-size-big: 25px;
    --font-size-small: 14px;
}

body {
    background-color: var(--bg-color);
    font-size: var(--font-size-big);
}
h1 {
    color: var(--font-color, #00f);
}
.container {
    background-color: var(--bg-second);
    color: var(--font-color);
}

@media (max-width: 450px) {
    body {
        font-size: var(--font-size-small);
    }
}
```

### [Correto] Mudar o valor da variável a partir do media query

Em vez de parar de usar variável dentro da media query como no primeiro [Errado], ou apenas criar varias variáveis para mesma função com valor diferente como no segundo [Errado], Já na forma [Correto] Simplesmente inicia um novo `:root` dentro do @media e colocamos a variável e o valor de acordo com o que queremos para aquele @media.

```css
:root {
    --bg-color: #fff;
    --bg-second: #ccc;
    --font-size: 25px;
}

body {
    background-color: var(--bg-color);
    font-size: var(--font-size);
}
h1 {
    color: var(--font-color, #00f);
}
.container {
    background-color: var(--bg-second);
    color: var(--font-color);
}

@media (max-width: 450px) {
    :root {
        --font-size: 15px;
    }
}
```

# Hack CSS : Altura relativa a largura.

Tornando uma incorporação de vídeo do youtube responsivo, primeiro criaremos uma `<div>` que ira funcionar como um container para área do vídeo, e dentro desta outra `<div>` para ter a área especifica mesmo do vídeo, e dentro dessa ultima `<div>` colocamos o `<iframe>` 

### Como ficara o HTML

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsividade</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <h1>Titulo de site</h1>

    <div class="video">
        <div class="video-area">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/xZXj5j5U8HQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>
</body>
</html>
```

Agora as modificações dentro do CSS, dentro das `<div>` e também no `<iframe>` , na primeira `<div>` Colocamos a largura que queremos, assim não adicionando um propriedade height(altura) a mão ela será proporcional as regras que definirmos na próxima `<div>`

### Ficando desta forma:

```css
.video {
    width: 600px;
}
```

Na segunda `<div>` iremos adicionar um `position: relative` Colocar a altura como zero `height: 0px` este background-color que adicionamos é apenas para percebermos caso saia a intenção não e que ele aparece ou que o mantenha, e a magica vem no `padding: 0px 0px 50%;` onde esse valor em porcentagem define a proporção, ou seja, caso esteja 100% a proporção e de um quadrado os dois lados serão iguais, caso coloque 50% a altura(height) terá metade da largura(width)

Técnica rápida para descobrir proporção em porcentagem, por exemplo o 16/9 o mais usado em telas, dividimos a altura pela largura, no caso do Full HD (1080x1920) 1080/1290 = 0,5625 Multiplicando esse valor por 100 teremos a porcentagem, 0,5623*100 = 56,25.

### Ficando desta forma:

```css
.video {
    width: 600px;
}
.video-area {
    position: relative;
    height: 0px;
    background-color: #ccc;
    padding: 0px 0px 56,25%;
}
```

Agora dentro da nossa tag `<iframe>` que esta dentro da nossa segunda `<div>` , vamos adicionar a propriedade `position: absolute` e que ele pegue toda a área disponível da minha `<div>` com classe video-area.

### Ficando desta forma:

```css
.video {
    width: 600px;
}
.video-area {
    position: relative;
    height: 0px;
    background-color: #ccc;
    padding: 0px 0px 56.25%;
}
.video-area iframe {
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    border: 0px;    /*Alguns Navegadores coloca borda no iframe*/
}
```

O vídeo esta responsivo podemos testar pelo Inspecionar elemento do navegador, onde a gente alterando o valor de width da `<div>` com classe video ele se redimensiona, agora vamos deixar ele responsivo na tela, quando realmente for maior ou menor a área de visualização do usuário.

Primeiro adicionar `width` como 100% para ele cobrir todo o espaço disponível, que no caso e o tamanho que queremos que ele apareça originalmente, que esse tamanho iremos colocar no `max-width`, depois colocamos um `margin` como auto para o vídeo ficar no meio da tela.

### Ficando desta forma:

```css
.video {
    width: 100%;
    max-width: 600px;
    margin: auto; /*Para ficar no meio da tela*/
```

O vídeo ficara com 600px de width (largura) e vai se espremer na tela ate não caber mais, ai vai começar a se redimensionar com a proporção que colocamos no .video-area

### Possíveis Duvidas:

Pergunta:

Eu sei pra que serve a margin e tal, mas queria entender para que servem esses códigos na classe
.video-area iframe:
.video-area iframe{
top: 0px;
bottom:0px;
left: 0px;
Entendo que está setando a margin como 0px, mas a técnica funcionou normalmente mesmo removendo esse código.
Pode usar sem esses parâmetros ou é uma boa prática configurá-los?

Resposta:

Então mano, isso está relacionado com como a propriedade position funciona.
A propriedade position define qual o ponto de referencia que será utilizado para posicionar ele objeto e as propriedades que posicionam ele são as: top, left, right e bottom.
Ex: no relative, o ponto é ele mesmo, por isso essas propriedades tem o mesmo efeito de aplicar um margin no elemento, no absolute, a referencia é o elemento ancestral mais próximo com position relative ou a tag html, por isso quando as propriedades são utilizadas, o elemento se move em relação as bordas correspodentes do elemento de referencia (tipo de cair no HTML, como ele representa a página, e nós utilizarmos top: 0; left: 0; o elemento vai se posicionar no canto superior esquerdo da página).

E tem um truque que podemos utilizar com essas propriedades e o position: absolute em que se nós definirmos duas extremidades (top e bottom ou left e right) como zero, elas atuam como aquela dimensão 100% (tipo top e bottom 0 resulta num resultado igual a height: 100%;), então no caso desse código, você pode utilizar ou width e height como 100% ou utilizar top, left, right e bottom como 0. Logo não tem problema retirar essas propriedades e só utilizar elas quando for necessário.

Pergunta:

Eu não entendi muito bem o uso do padding, tipo como ele impacta na altura, se o height é 0 ? e padding num é um espaçamento interno ? eu fiquei boiando nessa coisa do padding 0px 0px e 56,25%(que é o espaçamento interno direcionado para baixo, porém como ele vai mostrar algo se o height é 0?)

Resposta:

Isso é um truque porque quando o padding excede o tamanho do elemento, ele tem prioridade sobre o tamanho do elemento, então se a altura é 0 e o padding-bottom é 50px, na prática é como se o elemento tivesse 50px de altura. O problema disso é que se o elemento tiver conteúdo dentro, então o calculo do padding fica bugado e provavelemente não se obterá o efeito visual desejado, e é por isso que nessa aula é usado o position absolute, assim o elemento que realmente tem o conteúdo, sempre fica do tamanho da div que vai ser o espaço (ou seja tem o padding).