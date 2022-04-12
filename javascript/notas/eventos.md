# Introdução
Uma das possibilidades do javascript e ele reagir a algum acontecimento(evento), por exemplo um clique em um botão.

# `this` **Muito Importante**
Do ingles isto/este, seleciona o próprio elemento, ou seja como no exemplo acima, seleciona o `<button>` sem que aja necessidade de dar `get` no elemento.

# `event`
Envia os dados detalhados do evento que ocorreu, por exemplo no evento de teclado, a tecla que foi digitada entre outras informações

# Eventos de mouse.
Basta em um editor com autocomplete digitar `onmouse` e ele da varias opções.

## Clique
`onclick` pode ser adicionado a qualquer elemento, ate mesmo em um h1 por exemplo.
```html
<button onclick="click()">Teste<button>
<button onclick="this.innerHTML = 'clicou'>Teste</button>
```
Assim que o evento de click acontecer, executara a função `click()`.
> Também e possível entre as aspas adicionar um código javascript direto.

## Mouse sobre
`onmouseover` como o hover no CSS
```html
<h1 onmouseover="console.log('passou o mouse')">Titulo</h1>
```

## Eventos de teclado.
Rasta em um editor com autocomplete digitar `onkey` e ele da varias opções.

`onkeyup` - Solta a tecla (Mais utilizado em campos de texto, pois conta a digitação completa, apertar e soltar.)
`onkeydown` - Preciosa a tecla.

### Exemplo
Quando o usuario digitar Ctrl + Enter ele pega o valor do campo e manda para o console

HTML
```html
<input onkeyup="digitou(event)" type="text" id="campo"/>
```
JAVASCRIPT
```javascript
function digitou(e) {
    if (e.keyCode == 13 && e.ctrlKey == true) {
        let texto == document.getElementById('campo').value;
        console.log(texto);
    }
}
```

