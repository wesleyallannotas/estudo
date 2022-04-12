# Introdução

Recurso adicionado com o ECMAScript 6, alguns lugares chama *desestruturação*, funciona com *Objetos* e *Arrays*, nada mais e do que selecionar itens específicos e jogar dentro de variáveis.  
A desconstrução do array deve ser feita em ordem que os items foi criado.

# Sintaxe

> Como array não tem um nome para o item e sim números em sequenciá gerados automaticamente, quando vamos descontrair precisamos dar um nome para a variável, e ele pegara os items em sequenciá.
> Basta deixar o item em braco com para pular.(Deixar espaço entre as virgular vazias e opcional)
```javascript
// Base
let [nomeitem, nomeitem...] = arrayDesconstruir
// Pular Items
let [nomeitem, , , nomeitem...] = arrayDesconstruir
```

# Criando Varias Variáveis

Usa este conceito para criar varias variáveis de uma vez, pois assim como no objeto podemos adicionar valor em itens inexistente.
```javascript
let [nome, sobrenome, idade = 90] = ['Wesley', 'Silva'];
```

# Exemplo

```javascript
let array = [ 'Wesley Silva', 'Wesley', 'Silva'. '@wesleyallansilva'];
let [nomeCompleto, nome, sobrenome, instagram] = array;

console.log(nomeCompletom nome, sobrenome, instagram);
```
