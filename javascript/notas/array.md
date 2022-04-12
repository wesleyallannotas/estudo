# Introdução
Adicionar em uma variável vários valores ordenados numericamente, array **aceita todo tipo de item inclusive funções**  
Ate mesmo array dentro de array e objetos.

# Sintaxe
Adicionar valores dentro e colchetes, separados por virgulas
```javascript
let carros = ['valor1', 'valor2', 'valor3', 'valor4', 'valor5'];
// OU
let carros = [
    'valor1',
    'valor2',
    'valor3',
    'valor4',
    'valor5'
    45
    56
    function() {
        console.log("funcao dentro dee arra");
    }
    ];
// FORMA ANTIGA NAO MAIS USADA
let carros = new Array('valor1', 'valor2', 'valor3', 'valor4', 'valor5');


console.log(carros); // Exibe uma lista com todos
consolo.log(carros[1]) //Exibe o segundo valor (começa contar do 0) 
```