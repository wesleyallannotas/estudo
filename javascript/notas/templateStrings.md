# Introdução

Recurso recente, utilizado para criar **códigos mais legíveis**.  
Reconhecido como *template strings* quando se encontra entre `` em vez de aspas simples ou duplas.

# Modo antigo
>Ainda funcional, e usado.
```javascript
let nome = 'Wesley';
let idate = 24;
let frase = 'Meu nome e '+nome+', e eu tenho '+idade+' anos e ano que vem eu farei '+(idate+1)+' anos';
console.log(frase);
```

# Template Strings (Modo Novo)
```javascript
let nome = 'Wesley';
let idate = 24;
let frase = `Meu nome e ${nome} e eu tenho ${idade} anos e ano que vem eu farei ${idade+1}`;
console.log(frase);
```