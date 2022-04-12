# Introdução

*CSS* e utilizado para adicionar estilo ao documento *HTML*.

# Sintaxe
**Seletor {propriedade: valor;}**  
Seletor - Recebe o CSS  
Propriedade - O que sera alterado/adicionado  
Valor - Alteração  

# Como Adicionar

Podemos adicionar *CSS* de 3 formas diferentes em nossa documento *HTML*, sendo elas Inline, Interna e Externa.

## Inline

Pode ser adicionado *CSS* diretamente no elemento (tag) através do atributo `style`
```HTML
<div style="color:blue;font-size:20px;"></div>
```

## Interno

*CSS* interno e adicionado no *HEAD* do documento HTML, dentro das tag `<style>` se adicionar o CSS.
```HTML
<head>
    <title>Exemplo</title>
    <style>
        h1 {
            font-size: 20px;
            text-style: italic;
        }
    </style>
```

# Externo

*CSS* externo e quando se cria um arquivo com a extensão `.css` e este arquivo se conecta ao HTML através da tag `<link>`.
```HTML
<head>
    <title>Exemplo</title>
    <link href="LocalizaçãoDocumento" rel="stylesheet"/>
</head>
```

# Seletores Básicos

Podemos selecionar nossos elementos de 3 formas básicas, através da tag, class e ID.

## Tag
Basta adicionar a tag
```css
h1 {
    color: red;
}
```

## Class

Basta digitar um ponto(.) antes do nome da classe adicionada através do atributo `class`.  
**Mais usado**
```css
.menu {
    background-color: red;
}
```

## ID

Basta digitar uma cerquilha antes do nome do ID adicionado através do atributo `id`.  
**Usar com cuidado tem outros usos mais interessantes do que so colocar CSS**
```css
#menu {
    background-color: red;
}
```

# Seletores Avançados

Seletores avançador utilizados em situações especificas

## Seletor por Atributo

Seleciona elementos que possuam aquele atributo especificado.
```css
/* Seleciona todas as tag que possuam o atributo required */
[required] {
    color: red;
}

/* Seleciona todos as tag input que possuam o atributo required */
input[required] {
    color: red;
}

/* Seleciona pelo valor do atributo */
input[type=text] {
    color: red;
}

/* Atributos com valores nao padrões do HTML, ou seja escolhas do programas, tem que adicionar aspas */
input[name="Username"] {
    color: red;
}

/* Selecionando através de parte do valor do atributo */
/* Qualquer parte do valor do atributo href */
a[href*="economia"] {
    Color: red;
}
/* Pelo inicio do valor do atributo */
a[href^="http"] {
    color: red;
}

/* Pelo final do valor do atributo */
a[href$=".com"] {
    color: red;
}
```
>No lugar da tag em si, pode ser usar class ou ID também, so seguir a regras de como chama-las, ponto na class e cerquilha no atributo
>

## Seletor por Elemento Vazio

Seleciona o elemento que estiver vazio
```css
/* Seleciona a div que estiver vazia */
div:empty {
    background-color: red;
}
```

## Seletor por Conteúdo do elemento

Através dessa forma podemos atribuir CSS em partes especificas do conteúdo, por exemplo aumentar a primeira listra dos parágrafos.
```css
/* Selecionando apenas a primeira letra do paragrafo */
p::first-letter {
    font-weight: bold;
    font-size: 50px;
}

/* Selecionando a primeira linha do elemento */
p::first-line {
    background-color: yellow;
}
```
>Utilizamos duas vezes dois pontos pois estamos selecionando uma parte do conteúdo do elemento, nao o elemento todo.

## Seletor através da posição do elemento
Seleciona o elemento através da ordem que ele se encontra no documento HTML

```css
/* Seleciona o primeiro elemento */
div:first-child {
    background-color: red;
}

/* Seleciona o ultimo elemento */
div:last-child {
    background-color: red;
}

/* Seleciona o elemento especifico */
div:nth-child(2) {
    background-color: red;
}
```
> Diferente o Javascript e muitas outras linguagens que a contagem se inicia do 0, no css se inicia de 1.

## Seletor Negativo

Exclui um elemento da seleção, ou seja seleciona todos os outros menos aquele.
```css
/* Seleciona todos os elementos menos o p */
:not(p) {
    background-color: red;
}

/* Seleciona tudo menos o p dentro da div */
div :not(p) {
    background-color: red;
}
```

## Seletor Before/After

Seletor utilizado em larga escala no mundo avançado do CSS, sempre seguido da propriedade `content` para inserir conteúdo, basicamente ele **cria um pseudo elemento onde podemos adicionar conteúdo**, porem na pagina final esse conteúdo funcionara como visual, ou seja, se adicionar um texto nem possível selecionar sera.
```css
.div2::before {
    content: "";
    display: inline-block;
    width: 3px;
    height: 10px;
    background-color: red;
}

.div3::after {
    content: ">>";
    color: red;
    font-weight: bold;
}
```
>So ingles before(antes) after(depois), normalmente para adicionar conteúdo antes e acima se usa before, e para aplicar depois e embaixo e usa after.
>