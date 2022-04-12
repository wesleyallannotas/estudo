# Introdução

Muito usado dos *Frameworks*, funciona tanto para *Arrays* quanto para *objetos*, sendo adicionado para *objetos* mais recentemente, utilizado quando queremos ter os mesmos items de uma *Array/Objeto* dento de outro.

# Sintaxe

```javascript
// Com Operador Spread
let numbers = [1,2,3,4];
let newNumbers = [...numbers,5,6,7]
console.log(newNumbers);
// resultado: Array [1,2,3,4,5,6,7];

// Sem Operador Spread
let numbers = [1,2,3,4];
let newNumbers = [numbers,5,6,7]
console.log(newNumbers);
// resultado: Array [Array[4],5,6,7]
```
> Caso nao utilizasse o *Operador Spread*, ou seja, coloca-se o nome do *Array/Objeto* sem os pontos, ele iria adicionar uma *Array/Objeto*, e nao os items soltos.

> Exemplo de uso de Operador Spread e Operador Rest, na nota do Operador Spread