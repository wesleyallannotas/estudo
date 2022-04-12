# Como declarar
Pode ser declarado variáveis e constantes no javascript de 3 formas, sendo elas `var`, `let` e `const`.
- Preferencia usar `let` para variáveis.
- Nao podemos criar variáveis com palavras reservadas.
- Nao pode começar o nome de uma variavel com um número.
- Nao pode conter espaços ou traços
- Utilizamos camelCase

# var
Escopo: Global
Redeclarar: Aceita
Alterar valor: Aceita
```javascript
var nome; // Declarou a variável
nome = 'Wesley'; // Inicializando a variável
var nome = "Wesley"; // Declarando e Inicializando ao mesmo tempo
nome = "Andressa"; // Alterar Valor
``` 
# let
Escopo: Local
Redeclarar: Nao aceita. 
Alterar valor: Aceita
```javascript
let nome; // Declarou a variável
nome = 'Wesley'; // Inicializando a variável
let nome = "Wesley"; // Declarando e Inicializando ao mesmo tempo
nome = "Andressa"; // Alterar Valor
``` 
# const
Escopo: Local
Redeclarar: Nao aceita
Alterar valor: Nao aceita (Apenas arrays e objetos)
> Aceita que muda o valor das propriedades e nao que altere a variável inteira, ou seja estrutura.
```javascript
const nome = "Wesley";
const nome = {nome:'Wesley', sobrenome:'Silva'};
nome.nome = 'Pedro';
```