As contas em javascript seguem o padrão **IEEE 754-2008**

# `toString()`

Transforma em string.
```javascript
let n = 10;

let res = n.toString();

console.log(res);
```

# `toFixed(x)`

Como parâmetro colocamos a quantidade de decimais queremos exibir.
```javascript
let n = 10.56844723;

let res = n.toFixed(2);

console.log(res);
```

# `Number.isInteger(x)`

Retorna um Boolean que verifica se o **numero e um inteiro**.
```javascript
let num1 = 10
let num2 = 10.25
console.log(Number.isInteger(num1));
// resultado: true
console.log(Number.isInteger(num2));
// resultado: false (Pois e um numero de ponto flutuante)
```

# `Number.IsNaN(x)`

Retorna um Boolean que verifica se e um NaN(Not a Number)

```javascript
let temp = 10 * 'Ola';
console.log(Number.inNaN(temp))
// resultado: true (Nao tem como fazer um number multiplicado por uma string de letras)