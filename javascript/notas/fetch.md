# Introdução

Função do javascript, `fetch()` retorna uma *Promise*, *fetch* possui majoritariamente dois parâmetros, sendo o segundo opcional.  
- Url da requisição  
- Object onde colocamos as configurações da requisição (Por padrão, ou seja, caso nao adicione nada, GET)  
Usando o `then()` do `fetch()` recebermos um object do tipo *Response*.

# `json()`

Apos recebermos via *fetch* podemos converter para JSON através da função, porem ela retornara uma *Promise* assim sendo necessário o uso de `then()` novamente.

# Exemplo de uso

> Continuação na nota "AsyncAwait.md"
```javascript
function loadPost() {
    // Mensagem de Load
    document.getElementById('posts').innerHTML = "Carregando...";
    //Requisição
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(function(resultado){
            return resultado,json();
        })
        .then(function(json){
            montarBlog(json);
        })
        .catch(function(error){
            console.log("Deu problema!");
        });
}
function montarBlog(lista) {
    let html = '';
    // for(let i=0;i<lista.length;i++) // Forma Clássica
    for(let i in lista) {
        html += '<h3>'+lista[i].title+'<h3>';
        html += lista[i].body+'<br/>';
        html += '<hr/>';
    }
    document.getElementById('posts').innerHTML = html;
}
```

# fetch com POST

Usando o método de envio *POST*  
Partindo que temos um HTML com um `<button>` com o atributo `onclick` executando a função `inserirPost()`
> Utilizando Async e Await, notas encontradas no arquivo "AsyncAwait.md"
```javascript
async function inserirPost() {
    // Mensagem de Load
    document.getElementById("posts").innerHTML = "Carregando...";
    // Requisição
    let req = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST'
        body: JSON.stringify({
            title: 'Titulo de Teste',
            body: 'Corpo de Teste',
            userID: 4
        }),
        headers: {
            'Content-type': 'application/json'
        }
    });
    let json = await req.json();
    console.log(json);
}
``` 