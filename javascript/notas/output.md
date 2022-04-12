# Formas de mostrar
Basicamente existe 4 formas de exibir informas do javascript para o usuário.

# No Documento
## Manipulando o documento HTML
Adicionado um id ao elemento que vai ser manipulado.  
Exemplo um `<h2>` com *id* titulo
```javascript
document.getElementById("titulo").innerHTML = "Opa, tudo bem?";
```

## Adicionando ao documento
Através de `documento.write` podemos adicionar o que quisermos ao documento html.
```javascript
document.write("<div><p>Teste de documento write</p></div>");
```

# Através da janela
Ou seja pelo navegador não dentro do documento HTML, com o navegador exibindo um popup.
```javascript
window.alert("Mensagem de exemplo");
//atalho
alert("Mensagem de exemplo");
```
# Através do console
Usando o comando `console.log()` podemos enviar mensagem para o console.
```javascript
console.log("Mensagem digitada 'aqui' aparecera no console");
console.log('Mensagem digitada "aqui" aparecera no console');
console.log(`Mensagem 'digitada' aqui "aparecera" no console`);
```

# Proteger o texto
Usamos as aspas pos queremos que exiba aquele texto ou seja, literal, sem as aspas ele buscaria uma variável, **serão considerados *strings***  
Sendo possível utilizar:  
- Aspas simples (')
- Aspas duplas (")
- Crases (`) - Utilizado para fazer template string

# Exibir números
Para exibir números nao utilizamos nenhuma forma de protetor, **Sendo considerado um *number*** 
```javascript
console.log(12345);
```