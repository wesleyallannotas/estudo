# Introdução

Como exibir um Thumbnail de uma imagem sem que seja necessário o upload.  

# Exemplo de uso

JS para uma pagina HTML com um `<input type="file" accept="image/" id="imagem"` e um `<button>` com o atributo `onclick` contendo o valor `mostrar()`, onde a thumbnail sera exibida em uma `<div>` com o atributo `id` recebendo como valor `area`
```javascript
// Método Síncrono
function mostrar() {
    let imagem = document.getElementById('imagem').files[0];

    let img = document.createElement('img'); // Objeto que vai se transformar em elemento
    img.src = URL.createObjectURL(imagem);
    img.width = 200;

    document.getElementById("area").appendChild(img);
}
```

# Thumbnails com FileReader

Mesmo HTML do exemplo anterior, desa vez utilizando o `FileReader()`(Web APIs)  
- `onloadend` - Quando o carregamento acabar
- `readAsDataURL` - Usa o *Reader* para ler a imagem
```javascript
// Método Assíncrono
function mostrar() {
    let reader = FileReader();
    let image = document.getElementById('imagem').files[0];
    
    reader.onloadend = function() {
        // reader.result // result tera a url da imagem
        lei img = document.createElement('img');
        img.src = reader.result;
        img.width = 200;
        document.getElementById('area').appendChild(img);
    }
    reader.readAsDataURL(imagem);
}
```
