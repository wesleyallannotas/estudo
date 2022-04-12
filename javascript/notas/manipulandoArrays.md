# Transformar

## `toString()`

Transforma *array* em um *string* **separando** itens em **virgulas**.
```javascript
let lista = ['Ovo', 'Farinha', 'Massa'];

let res = ;

console.log(res);
```

## `join(x)`

Transforma *array* em *string* onde atribuímos como **parâmetro um separador**.
> Diferente do `toString()` que por padrão e como única opção o separador e virgula.
```javascript
let lista = ['Ovo', 'Farinha', 'Massa'];

let res = lista.join('-') ;

console.log(res);
```

# Filtragem de dados 

## `indexOf(x)`

Semelhante ao usado na *string* com a diferença que ele traz como resposta a posição do item.
> Se nao encontrar retorna `-1`
```javascript
let lista = ['Ovo', 'Farinha', 'Massa'];

let res = lista.indexOf('Farinha') ;

console.log(res);
```

# Modificar

## `pop()`

Remove o **ultimo** item do *array*
> Atenção ele altera o próprio *array*
```javascript
const plants = ['broccoli', 'cauliflower', 'cabbage', 'kale', 'tomato'];

console.log(plants.pop());
// expected output: "tomato"

console.log(plants);
// expected output: Array ["broccoli", "cauliflower", "cabbage", "kale"]

plants.pop();

console.log(plants);
// expected output: Array ["broccoli", "cauliflower", "cabbage"]
```

## `shift()`

Remove o **primeiro** item da *array*
> Atenção ele altera o próprio *array*
```javascript
const array1 = [1, 2, 3];

const firstElement = array1.shift();

console.log(array1);
// expected output: Array [2, 3]

console.log(firstElement);
// expected output: 1
```

## `push(x)`

Adicionar item no final da *array*
> Atenção ele altera o próprio *array*
```javascript
const animals = ['pigs', 'goats', 'sheep'];

const count = animals.push('cows');

console.log(count);
// expected output: 4
console.log(animals);
// expected output: Array ["pigs", "goats", "sheep", "cows"]
```

## Alterar item especifico

Seleciona o item dentro da array e altera ele.
> Caso seleciona um item que nao existe, ele então sera **adicionado**, porem mais recomendado utilizar o `push()`
```javascript
let lista = ['Ovo', 'Farinha', 'Corante'];

lista[0] = 'Queijo';

console.log(lista);
// expected output: Array ['Queijo', 'Farinha', 'Corante']
```

## `splice(x,y)`

Apagar um ou mais item especifico da *array*
> Atenção ele altera o próprio *array*
- x - A partir de qual item quer remover 
- y - Quantos items quer remover.
```javascript
let lista = ['Ovo', 'Farinha', 'Corante']

lista.splice(1, 1);

console.log(lista);
// expected output: Array ['Ovo', 'Corante']
```

## `concat()`

Concatenar ou seja, somar.
```javascript
let lista = ['Ovo', 'Farinha', 'Corante'];
let lista2 = ['Batedeira', 'Forno', 'Prato'];

let res = lista.concat(lista2);

console.log(res);
// expected output: Array ['Ovo', 'Farinha', 'Corante', 'Batedeira', 'Forno', 'Prato']
```

## `sort()`

Ordena por padrão em alfabético os itens da *array*
> Atenção ele altera o próprio *array*
```javascript
let lista = ['Ovo', 'Sal', 'Farinha', 'Corante'];

lista.sort();

console.log(lista);
// expected output: Array ['Corante', 'Farinha', 'Ovo', 'Sal']
```

## `reverse()`

Inverte a ordem do *array*
> Atenção ele altera o próprio *array*
```javascript
let lista = ['Ovo', 'Sal', 'Farinha', 'Corante'];

lista.reverse();

console.log(lista);
// expected output: Array ['Corante', 'Farinha', 'Sal', 'Ovo']
```

# MAP

Usando o `map()` criamos dentro de *map* uma função que percorrera item a item rodando a função e jogando o resultado em uma nova *array*, ou seja, **nao altera a *Array* original**.
```javascript
let number = [10, 20, 30, 40, 50];
let number2 = [];

// exemplo de map multiplicando todos os valores por 2.
number2 = number.map(function(item) {
    return item * 2;
});

console.log(number2);
// expected output: Array [20, 40, 60, 80, 100]
```
> Recebera como parâmetro os items da *array*, nesta caso dei o nome da variavel de parâmetro como item.

# FILTER

Vem da ideia de filtrar.  
Dentro de `filter()` colocamos uma função, que retornara um Boolean, sendo *true* aproveita o item, sendo *false* nao aproveita.
```javascript
let number = [40, 5, 2, 34, 19, 24];
let number2 = [];

// exemplo de filter, aproveitando apenas o items menores que 20.
number2.filter(function(item) {
    if(item < 20) {
        return true;
    } else {
        return false;
    }
});

console.log(number2);
// expected output: Array [5, 2, 19]
```

# EVERY

Dentro de `every()` colocamos uma função, que retornara um Boolean, e como resultado final **devolvera um Boolean**.  
Por exemplo, **todos** os itens da array retornaram *true*, então, ele retornara *true*.  
Caso um ou mais items retorne *false* ele retornara *false*.  
> Serie o "e" "&&" todos tem que ser *true* para devolver o resultado como *true*
```javascript
let num = [1, 5, 23, 26, 50, 15, 11];
let verifica

verifica = num.every(function(item) {
    if(item < 20) {
        return true;
    } else {
        return false;
    }
});

console.log(verifica);
// expected output : false
```

# SOME

Significa algum em ingles, dentro de `some()` colocamos uma função, que retornara um Boolean, e como resultado final **devolvera um Boolean.**  
Por exemplo, **algum** os itens da array retornaram *true*, então, ele retornara *true*.
> Seria o "ou" "||" algum sendo *true* ja devolve como resultado *true*.  
```javascript
let num = [1, 5, 23, 26, 50, 15, 11];
let verifica

verifica = num.some(function(item) {
    if(item < 20) {
        return true;
    } else {
        return false;
    }
});

console.log(verifica);
// expected output : true 
```

# FIND

Procura no array, dentro de `find()` colocamos uma função, que retornara o item "buscado", ou seja, que a função retorne *true*. 
```javascript
let num = [1, 5, 23, 26, 50, 15, 11];
let num2 = []; 

num2 = num.find(function(item) {
    if(item == 23) {
        return true;
    } else {
        return false;
    }
});

console.log(num2);
// expected output : Array [23];


// Exemplo de busca
let users = [
    {id:1, nome:'Wesley', sobrenome:'Silva'},
    {id:2, nome:'Thiago', sobrenome:'Lacerda'},
    {id:3, nome:'Antonio', sobrenome:'Conselheiro'}
];

let busca = users.find(function(item) {
    return (item.id == 2) ? true : false; // Forma simplificada do 'if' para retornar *true* ou *false*
});

console.log(busca);
```

## `findIndex()`

A diferença do `find()` e que ele nao retorna o item e sim a posição do item na *array*
```javascript
let num = [1, 5, 23, 26, 50, 15, 11];
let num2 = []; 

num2 = num.findIndex(function(item) {
    if(item == 23) {
        return true;
    } else {
        return false;
    }
});

console.log(num2);
// expected output : Array [23];
```