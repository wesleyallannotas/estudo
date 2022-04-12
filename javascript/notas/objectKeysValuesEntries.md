# Introdução

Funciona para *Objeto* e *Array*.

# Interação com *Array*

- `keys` - Exibe o numero do índice
- `values`  - Exibe os valores, ou seja, os items da *array*
- `entries` - Cria uma *array* para cada item, contendo o Valor e o Índice
```javascript
let list = ['ovo', 'carne', 'feijão']

console.log(Object.keys(lista));
// resultado: Array ['0', '1', '2']
console.log(Object.values(lista));
// resultado: Array ['ovo', 'carne', 'feijão']
console.log(Object.entries(lista));
// resultado: Array [Array[2], Array[2], Array[2]]
```

# Interação com *Objetos*

- `keys` - Exibe o nome dos items 
- `values`  - Exibe os valores dos items
- `entries` - Cria uma *array* para cada item, contendo o Valor e o nome do item.
```javascript
let pessoa = {
    nome:'Wesley',
    sobrenome:'Silva',
    idade:23
};

console.log(Object.keys(pessoa));
// resultado: Array ['nome', 'sobrenome', 'idade']
console.log(Object.values(pessoa));
// resultado: Array ['Wesley', 'Silva', 23] 
console.log(Object.entries(pessoa));
// resultado: Array [Array[2], Array[2], Array[2]]
```