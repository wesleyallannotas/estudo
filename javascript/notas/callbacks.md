# Introdução

*Callbacks* em javascript, e uma função que e criada para mandar para outra execução, geralmente uma execução assíncrona.
> CALLBACK = "I'm gonna call you back = Eu te ligo de volta" 
>
Função que sera criada, para ser executada quando determinada situação ocorrer.
```javascript
// Exemplo de Callback
function alertar() {
    alert("Opa, tudo bem?");
}
setTimeout(alertar, 2000);
```
> Va ao servidor e peça a informação, quando tiver essa informação, executa tal função

Tem callbacks que não são assíncronas (e por isso param sim a execução do código) por exemplo as que a gente passa para os métodos relacionados a arrays como map, forEach e etc. Uma definição mais simples de callbacks, seria o nome que a gente dá para uma função quando ela é passada como parâmetro.  
Então podemos entender que increment é uma função:
```javascript
const increment = x => x + 1;
```
Mas no momento em que increment é passada como parâmetro de outra função, por exemplo a map dos arrays, ela é considerada uma função callback:
```javascript
const incrementedNumbers = [1, 2, 3].map(increment)
```
Ela é uma callback pois em algum momento depois que ela for passada como parâmetro, ela será "chamada de volta" pela função que recebeu ela como parâmetro.