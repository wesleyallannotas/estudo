# Introdução

Métodos que strings possuem nativamente e podemos utilizar para manipular ou encontrar informação.  
**Strings sao indexadas** com cada carácter recebendo um numero partindo do 0, assim como na *Array* podemos ter acesso ao item que contem em determinado índice com a sintaxe `variavel[0]` com o 0 sendo índice a ser exibido.
> Assim como no ShellScript para escapar caracteres se utiliza "\"

# Filtragem de dados 

## `length`

Exibe a quantidade de caracteres dentro de uma string.
> Length começa a contar a partir do 1 normalmente, ou seja, uma string com length de 6 caracteres, tem seu ultimo carácter com o índice 5 pois a contagem de índice começa do 0

```javascript
let nome = 'Wesley Allan da Silva';

console.log(nome.length);
```

## `indexOf(x ,y)`

> Existe uma variação `lastIndexOf` funciona da mesma forma porem le do lado ao contrario começa do fim para o começo
Posição na string ou ate se existe.
- x - O que busca.
- y - (opcional) a partir de qual índice vai buscar.

```javascript
let nome = 'Wesley Allan da Silva';

console.log(nome.indexOf('Allan'));
```
> Retorna `-1` caso nao encontro o pedido na string.

# Extrair informação

## `slice(x,y)`

Pega um pedaço da string.  
Dois parâmetros com apenas o **primeiro sendo obrigatório**
- x - Posição inicial
- y - Posição final (Opcional)
> Colocando numero negativo ele começa a contagem do fim da string.

```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.slice(0, 6);

console.log(resultado);
```

## `substring(x,y)`

Funcionamento parecido com o `slice()` a diferença que ele **so funciona com números positivos.**


```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.substring(0, 6);

console.log(resultado);
```

## `substr(x,y)`

Parecido com os anteriores porem **difere no segundo parâmetro**, sendo o **segundo parâmetro a quantidade de caracteres que vai pegar.**
> Funciona números negativos.

```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.substr(-1, 6);

console.log(resultado);
```

## `charAt(x)`

Mostra o caractere naquela posição selecionada.

```javascript
let nome = 'Wesley';

let resultado = nome.charAt(2);
// let resultado = nome[2]; // Forma simplificada, a partir de 2009

console.log(resultado);
```
> A partir de 2009, se tornou possível ter o mesmo resultado de forma simplificada.

# Substituir

## `replace(x,y)`

Recebe dois parâmetros, no caso o primeiro e o que ele deve pesquisar dentro da string, e o segundo o que colocara no lugar do texto selecionado.
> Replace aceita expressões regulares.

```javascript
let nome = 'Wesley Allan da Silva';

// nome = nome.replace('Allan', 'Silva'); // Alterando a original.

let resultado = nome.replace('Allan', 'Silva');

console.log(resultado);
```
> No exemplo a cima a alteração esta na variavel resultado, ou seja, a variavel nome se mantém inalterada.

## `toUpperCase()`

Transforma a string inteira em caixa alta ou seja, maiúsculo.

```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.toUppercase();

console.log(resultado);
```

## `toLowerCase()`

Transforma a string inteira em caixa baixa ou seja, minusculo.

```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.toLowerCase();

console.log(resultado);
```

## `concat(x...)`

Utilizado para concatenar texto na string.
> Pode colocar **quantos parâmetros quiser**, assim concatenando em sequencia.

```javascript
let nome = 'Wesley';

let resultado = nome.concat(' Silva');

console.log(resultado);
```
> Existe mas nao e muito utilizada por existir formas mais simples de concatenar texto em uma string.

## `trim()`

Tira todos os espaços.
> Muito util, amplamente utilizado.

```javascript
let nome = '       Wesley       ';

let resultado = nome.trim();

console.log(resultado);
```

# Transformação

## `split(x, y)`

Transformando *string* em *array*  
Split significa dividir, utilizamos um parâmetro para informar o divisor.
- x - Divisor
- y - (opcional) quantas vezes ira fatiar.

```javascript
let nome = 'Wesley Allan da Silva';

let resultado = nome.split(' ');

console.log(resultado);
```
> Cada palavra fica ocupando um item da array gerada.

## `parseInt(x)`

Transforma a string em numero.

```javascript
let n = 10;

let resultado = parseInt(n) + 5;

console.log(resultado);
```

## `parseFloat(x)`

Preserva os decimais na transforma de *string* para *number*

```javascript
let n = 10.5;

let resultado = parseFloat(n);

console.log(n);
```