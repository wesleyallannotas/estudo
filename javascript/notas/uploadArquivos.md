# Introdução

Como enviar arquivos com JS através de requisição interna. 
`.files` gera um *FileList*, um objeto contendo todos os itens enviados, onde neste exemplo estamos escolhendo o primeiro *File*, onde cata *File* contem o arquivo e todas as informações dele.  
Geralmente se envia arquivos pelo método `POST`, onde o body da requisição e feito utilizando `FormData()`(Web APIs) uma classe de objeto.  
JS de uma HTML com um `<input/>` com atributo `type` com o valor `file` onde possui um `id` com o valor `arquivo` e um `<button>` com o atributo `onclick` carregando a função `enviar()`
```javascript
async function enviar () {
    let arquivo = document.getElementById('arquivo').files[0];

    let body = new FormData();
    body.append('title', 'Bla bla bla');
    body.append('arquivo', arquivo);

    let req = await fetch('https://www.urlrecebe.com.br/upload', {
        method: 'POST',
        body: body,
        headers: {
            'Content-type': 'multipart/form-data'
        } 
    })
}
```