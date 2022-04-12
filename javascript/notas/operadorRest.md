# Introdução

*Operador Rest*, sua sintaxe lembra o *Operador Spread*, porem o utilizamos quando nao sabemos quando parâmetros iremos receber, utilizando o *Rest* ele ira adicionar os parâmetros em uma *Array*

# Sintaxe

```javascript
// Com Operador Rest
function exibeNumeros(...numeros) {
    console.log(numeros;)
}
exibeNumeros(1,2,3,4)
// resultado: Array: [1,2,3,4]

// Sem Operador Rest
function exibeNumeros(numeros) {
    console.log(numeros;)
}
exibeNumeros(1,2,3,4)
// resultado: 1
```

# Exemplo *Spread* com *Rest*

```javascript
function adicionar(nomes, ...novosNomes) {
    let conjunto = [
        ...nomes,
        ...novosNomes
    ];
    return conjunto
}
let nomes = ['Wesley', 'Andressa'];

let maisNomes = adicionar(nomes, 'Adriana', 'Neia', 'Leonildo', 'Jose');

console.log(maisNomes);
// resultado Array ['Wesley', 'Andressa', 'Adriana', 'Neia', 'Leonildo', 'Jose']
```