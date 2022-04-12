# Introdução
DOM = Document Object Model  
Referencia de cada elemento da pagina aqui chamado de objeto, por isso *object*.  
Utilizado para manipular os elementos de uma pagina, ou seja, focado no javascript para web  

# Selecionando elementos
Existem algumas formas distintas de selecionar um elemento do documento, sendo elas.

## ID
Selecionar um elemento pelo id dele no HTML.
```javascript
document.getElementById('titulo');
```
> Note que element se encontra no singular pois o ID e único so um elemento pode ter o mesmo ID

## Class
Selecionar os elementos pela classe.
```javascript
document.getElementsByClassName('list');
document.getElementsByClassName('list')[0]; // Selecionando item da array.
```
> Note que *element* agora se encontra no plural, pois podemos tem a mesma classe em vários elementos, **Por causa disso sempre retornara um array, seja ela vazia, com um elemento apenas ou vários.

## Tag
Selecionando os elementos pela tag
```javascript
document.getElementsByTagName('div')
```
> Note que retorna uma array e elements se encontra no plural pois uma tag pode ser repetida.

## Name
Selecionar pelo name, atributo geralmente utilizado em `<input>`.
```javascript
document.getElementsByName('telefone');
```
> Retorna un array, e se encontra no plural pois podemos der inputs por exemplo com o mesmo name.

## querySelector
Com query selector, podemos selecionar um elemento como no css, `querySelector` sempre retorna o primeiro que encontrar, para selecionar todas e trazer o resultado como **array** se utiliza `querySelectorAll`.
- ID - `#id`
- class - `.class`
- tag - `tag`
```javascript
document.querySelector('.lista');
document.querySelector('.lista')[2];
document.querySelector('ol.lista');
```

# Alterando conteúdo elemento
Apos selecionar o elemento com sucesso, adicionar html dentro do elemento.
```javascript
document.getElementById('titulo').innerHTML = "Novo titulo";
document.querySelector('.titulo')[0].innerHTML = "Novo titulo";
```

# Manipulando Class do elemento
Utilizamos o `.classList` que retorna o objeto que controla as classes do elemento a partir dai podendo manipular.
```javascript
document.querySelector('#text').classList.add('verde');
document.querySelector('#text').classList.remove('verde');
```
Adicionou a classe de nome `verde` no elemento com id text.

# Manipulando Atributos
Possível manipular um atributo de duas formas, inserindo um valor no atributo, ou pegar o valor.
```javascript
function trocarImagem(filename) {
    document.querySelector('.image').setAttribute('src', './assets/images/'+filename);
}
```

## Pegar valor de um atributo
Possível pegar o dado para guardar em uma variável e exibir depois por exemplo.
```javascript
let alternativo = document.querySelector('.image').getAttribute('alt');
```

# Dimensões
Possível obter esses dados das dimensões de 3 diferentes formas.

## `offset` (offsetWidth, offsetHeight)
Engloba = width ou height, tamanho do scrollbar, padding e borda
```javascript
document.querySelector('.texto').offsetWidth
```
> Ignore o tamanho da scrollbar e a borda.

## `client` (clientWidth, clientHeight)
Engloba = width ou height e padding.
```javascript
document.querySelector('.texto').clientWidth
```

## `scroll` (scrollWidth, scrollHeight)
Engloba = width ou height real
> Ou seja, caso haja uma barra de rolante ele calcula todo esse conteúdo dentro da barra.
> Ignore o tamanho da scrollbar.

# Distâncias e Scroll Suave
Caso for manipular o navegador (window) caso for o documento HTML (document).

## Informação da Posição do Scroll
```javascript
window.scrollY // Eixo Vertical
window.scrollX // Eixo Horizontal

document.querySelector('.text').scrollTop // Eixo Vertical
document.querySelector('.text').scrollLeft //Eixo Horizontal
```
## Movimentar Scroll
```javascript
window.scrollTo(x, y) // x = eixo horizontal, y = eixo vertical.

document.querySelector('.texto').scrollTo(x, y) // x = eixo horizontal, y = eixo vertical.
```

## Movimentar Scroll (Suave)
Em vez de passar os dois parâmetros de forma comum, ira passar um **objeto** da seguinte forma.
```javascript
    window.scrollTo({
        top: 0,             // Eixo vertical
        left: 0,            // Eixo Horizontal
        behavior: 'smooth'  // Comportamento da rolagem
    })
```
> Behavior significa comportamento.