# Introdução
Funções sao amplamente utilizadas em todas as linguagens de programação, se baseá em um pedaço de código reservado com uma função distinta que assim que quiser utilizado basta chamar.

# Sintaxe
```javascript
function nomefuncao() {
    código
}
```

# Parâmetros
Parâmetros sao adicionado a função entre os parenteses.
```javascript
// Criando função
function alterar(titulo) {
    document.getElementById('titulo').innerHTML = titulo;
}
function soma(x, y) {
    let total = x + y;
    console.log(total);
}

// Chamando Função
alterar('Novo Titulo');
soma(10, 20);
``` 
> Usamos virgula para separar os parâmetros caso aja mais de um.

# `return`
Quando executamos uma função ela nao devolve nada como retorna, porem podemos atribuir o que queremos que ela retorne com o comando `return`
```javascript
function soma(x, y) {
    let total = x + y;

    return total;
}

var resultado = soma(10 + 20);
```
Desta forma definimos o que a função retorna de valor.  
Criei uma variável com o resultado da função soma de dois números, e como atribuímos para retornar a variável `total` que se encontra na função soma, teremos o valor dentro variável resultado.
> A função so devolve como resultado o que atribuímos como `return`, o que nao foi atribuído continuara ocorrendo quando chamar a função normalmente.

# Intervalo
Possível setar um tempo em **milissegundos** para executar determinada função
```javascript
setInterval(apareceBotao, 1000); // (nomefuncao, tempoemmilessegundos)
```
> Funcional porem consome processamento de tempos em tempos.

# Evento
Utilizando evento nao desperdiça processamento, pos so executara quando determinado **evento** ocorrer.
```javascript
window.addEventListener('scroll', apareceBotao);
```