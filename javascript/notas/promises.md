# Introdução

A tradução literal e Promessa, seu funcionamento remete a isto, pois **quando executamos uma requisição assíncrona ou um processo assíncrono, ficamos com uma especie de promessa de resultado.**  
Onde *Promises* nada mais e do que um resultado temporário, ou seja, uma promessa de que daqui um tempo teremos 3 opções de resultado.
- Esperando o resultado (pending)
- Deu certo (resolve)
- Deu errado (reject)
```javascript
function pegarTemp() {
    return new Promise(function(resolve, reject) {
        console.log("Pegando temperatura...");
        setTimeout(function(){
            resolve('40 na sombra');
            }, 2000);
    });
}
```
Em um promessa ou seja `Promise` e obrigatório ter duas funções, sendo elas `resolve` e `reject`, onde se usa o *resolve* para devolver o resultado de sucesso, e o *reject* para devolver resultado caso de errado.

# Como usar *Promise*

Usamos o `then`(E então) com um callback, exemplo usando a estrutura de *promise* criada anteriormente
> then = Quando tiver o resultado executa isto.
Sendo usado `then` quando tiver um *resolve*, ou seja, sucesso, e o `catch` quando tiver um *reject*, ou seja, seja resultado de erro.
```javascript
let tamp = pegarTemp();
temp.then(function(resultado){
    console.log("temperatura: "+resultado);
});
temp.catch(function(error){
    console.log("Eita, deu erro!");
});
```