# Introdução
Sera apresentado operadores **aritméticos**, de **atribuição** e **incremento**

# Aritméticos

Segui as regras de presidência da matemática, para alterar utilize parenteses.
```javascript
let a = 10;
let b = 5;
```
- `+` - Adição e concatenação (`a + b`)
- `-` - Subtração (`a - b`)
- `/` - Divisão (`a / b`)
- `*` - Multiplicação (`a * b`)
- `**` - Potencialização (`a ** b`)
- `%` - Resto da divisão (`a % b`)

# Incremento e Decremento

- `++` - Incremento (Adiciona 1 ao valor)
- `--` - Decremento (Diminui 1 do valor)
```javascript
let contador = 1;
// incremento pos
contador++; // resultado = 2
// incremento pre
++contador; // resultado = 3

let diminuidor = 10;
// decremento pos
diminuidor--; // resultado = 9
// decremento pre
--diminuidor; // resultado = 8
```
## pos e pre.  
- pre - Executa o incremento antes de determina ação
- pos - Executa o incremento depois de determinada ação
```javascript
let a = 1;
let b = 1;

console.log(a++); // exibe 1
console.log(a); // exibe 2

console.log(++b); // exibe 2
console.log(b); // exibe 2
```
> Se fazer o incremento ou decremento fora do console.log nao importa ser antes ou pos, exibira o resultado com a operação realizada.

## Atribuição

- `+=` - Atual mais algo
- `-=` - Atual menos algo
- `*=` - Atual multiplicado por algo
- `**=` - Atual potencializado por algo
- `/=` - Atual dividido por algo
```javascript
let a = 10;
let b = 2;

a += b; // resultado = 12 (Mesma coisa que `a = a + b`)
a -= b; // resultado = 8 (Mesma coisa que `a = a - b`)
a *= b // resultado = 20 (mesma coisa que `a = a * b`)
a **= b // resultado = 100 (mesma coisa que `a = a ** b`)
```