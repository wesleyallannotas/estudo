# Introdução

Javascript tem uma **classe** especifica para cálculos matemáticos, sendo ela `Math`

# Random
Por padrão retorna um numero aleatório entre 0 e 1.
```javascript
let number = Math.random();
```
Para escolher um numero máximo para essa `random`, utilizamos uma técnica com outra função.
```javascript
let number = Math.floor(Math.random() * 100); // Numero aleatório ate 100.
```

# PI

```javascript
Math.PI
```

# Arredondar numero

```javascript
let number = Math.round(3,67); //Arredonda para o mais proximo.
// resultado esperado: 4
let number = Math.floor(3.52); // Arredonda para baixo
// resultado esperado: 3
let number = Math.ceil(3,1); // Arredonda para cima
// resultado esperado: 4
```

# Numero Absoluto
```javascript
let number = Math.abs(-24);
// resultado esperado: 24
```

# min e max

Consiste e enviar os números e ele responder com o menor para `min` e o maior para `max`
```javascript
let number = Math.min(2, 56, 66, 5);
// resultado esperado: 2
let number = Math.max(2, 56, 66, 5);
// resultado esperado: 66
```