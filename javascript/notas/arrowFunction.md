# Introdução

Mais um forma de criar função, porem *Arrow Function* também chamada de **função anonima**, a gente nao tem o objeto `this`

# Sintaxe

Possível abrir chaves e criar a função com o `return` no final, ou caso nossa função nao precise executar nada e for **retornar algo** direto, invés de abrir chaves e criar o return, colocamos na frente da *Arrow*(=>) o que sera retornado.
> Quando possuir apenas um parâmetro o parenteses se torna opcional.
```javascript
// Forma 1
let soma = (x,y) => {
    return x + y;
}
// Forma 2
let soma = (x,y) => x + y;

// 1 Parâmetro
let letrasNome = nome => nome.length;

// Nenhum Parâmetro
let teste = () => teste;
```

# Formas Conhecidas
```javascript
// Padrão
function soma(x,y) {
    return x + y;
};
console.log(soma(10, 5)); // Utilizando

// Dentro de Variavel
let soma = function(x,y) {
    return x + y;
};
console.log(soma(10, 5)); // Utilizando

// Arrow Function
// Forma 1
let somar = (x,y) => {
    return x + y;
}
// Forma 2
let somar = (x,y) => x = y;
```