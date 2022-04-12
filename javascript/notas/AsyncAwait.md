# Introdução

Basicamente em um código assíncrono obriga o código "esperar" o resultado para prosseguir, **uma função que tem `async` tem dentro dela o `await`**

# Sintaxe

```javascript
// Padrão
async function loadPost() {}
// Arrow Function
let loadPost = async () => {}
```

# Exemplo de uso

> Código iniciado na nota "fetch.md"
```javascript
// SEM ASYNC AWAIT
// function loadPost() {
//     document.getElementById('posts').innerHTML = "Carregando...";
//     fetch('https://jsonplaceholder.typicode.com/posts')
//         .then(function(resultado){
//             return resultado,json();
//         })
//         .then(function(json){
//             montarBlog(json);
//         })
//         .catch(function(error){
//             console.log("Deu problema!");
//         });
// }
// COM ASYNC AWAIT
async function loadPost() {
    document.getElementById('posts').innerHTML = "Carregando...";
    let req = await fetch('https://jsonplaceholder.typicode.com/posts');
    let json = await req.json();
    montarBlog(json);
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