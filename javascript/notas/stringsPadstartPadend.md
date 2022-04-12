# Introdução

`padStart` e `padEnd` sao usadas para manipulação de *strings*, novidades do ECMAScripts, antes para ter o mesmo resultado era necessário muito código.  

# `padEnd(x,y)`
"End", ou seja, **preenche no final**
- x - Quantos caracteres a *string* tem que ter obrigatoriamente
- y - O que sera adicionado para a *string* atingir o requisito caso nao tenha por padrão
```javascript
let telefone = '542';
console.log(telefone.padEnd(9, '*'));
// resultado; 542******
```

# `padStart(x,y)`
"Start", ou seja, **preenche no inicio**
- x - Quantos caracteres a *string* tem que ter obrigatoriamente
- y - O que sera adicionado para a *string* atingir o requisito caso nao tenha por padrão
```javascript
let telefone = '542';
console.log(telefone.padEnd(9, '*'));
// resultado; ******542
```

# Exemplo de uso
Exemplo de exibir os últimos 4 números do cartão para o usuário confirmar.
```javascript
let cartao = '5443123243544333';
let lastDigits = cartao.slice(-4); // Pegou últimos 4 dígitos
let cartaoMascarado = lastDigits.padStart(16, '*'); // padStart asteriscos
console.log('Este e o seu cartao?'+cartaoMascarado);
// resultado: Este e o seu cartao? ************4333
```