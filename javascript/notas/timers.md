# Introdução

Criar *timers* ou seja, **intervalos** de tempo para que algo rode.

```javascript
// Função para exibir a hora.
function showTime() {
    let d = new Date();
    let h = d.getHours();
    let m = d.getMinutes();
    let s = d.getSeconds();
    let txt = h+':'+m+':'+s;
    document.querySelector('.horario').innerHTML = txt;
}

let timer = setInterval(showTime, 1000);
```

# `setInterval()`

Através do `setInterval()` podemos colocar como parâmetro o nome da função e o tempo em que ela rodara novamente em milissegundos.
> Repara que colocamos o nome da função sem as parenteses "()"
> Possível criar uma dentro do espaço do nome da função
```javascript
let timer = setInterval(função, tempomilesegundos);
```

# `clearInterval()`

Para o funcionamento do *timer*, **Atribuímos como parâmetro o nome da variavel que carrega o *timer***
> Para limpar o timer necessário que ele esteja dentro de uma variavel como no exemplo
```javascript
let timer; // Criar variavel fora para funcionar o parar
function comecar() {
    let timer = setInterval(showTime, 1000);
}
function parar() {
    clearInterval(timer);
}
```

# `setTimeout()`

Atribuímos um tempo em milissegundos antes da função começar a rodar, **funciona como tempo de espera**.
> Repara que colocamos o nome da função sem as parenteses "()"
> Possível criar uma dentro do espaço do nome da função
```javascript
setTimeout(function() {
    console.log("Rodou!");
}, 2000);
```

# `clearTimeout()`
Para o funcionamento do *timer*, ou seja, nao deixa ele rodar.
> Para limpar o timer necessário que ele esteja dentro de uma variavel como no exemplo
```javascript
let timer;
function rodar() {
    timer = setTimeout(function() {
        console.log('Rodou!')
    }, 2000);
}
function parar() {
    clearTimeout(timer);
}
```