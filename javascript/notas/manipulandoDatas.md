# Introdução

Date e uma classe de objeto que trás com sigo varias formas de manipular datas.
```javascript
let d = new Date();
console.log(d.toDateString()); // Forma mais resumida
console.log(d.toUTCString()); // Converte para o Horário mundial(GMT)
let d2 = new Date(2022, 0, 1, 12, 30, 12);
                // Ano, mes, dia, hora, minuto, secundo, milésimo
let d3 = new Date('2022-01-01 15:42:17'); // Date string
```
> Mes começa do zero(0) assim sendo janeiro o mes 0, caso for utilizar **Date string** nao se aplica.
> Mínimo necessário para gerar data ano e mes.
Criando desta forma ele vem com a data atual que foi criado, ou seja, do dispositivo que esta acessando.

# Pegando(get) os dados

```javascript
let d = new Date();
d.getFullYear(); // Ano por (AAAA)
d.getMouth(); // Mes (0 - 11)
d.getDay(); // Dia da semana (0 - 6)
d.getDate(); // Dia do mes
d.getHours(); // Hora
d.getMinutes(); // Minutos
d.getSeconds(); // Segundos
d.getMilliseconds(); // Milissegundos
d.getTime(); // Milissegundos des de 1-1-1970.
```

# Alterando(set) os dados
```javascript
let d = new Date();
d.setFullYear(); // Ano por (AAAA)
d.setMouth(); // Mes (0 - 11)
d.setDay(); // Dia da semana (0 - 6)
d.setDate(); // Dia do mes
d.setHours(); // Hora
d.setMinutes(); // Minutos
d.setSeconds(); // Segundos
d.setMilliseconds(); // Milissegundos
d.setTime(); // Milissegundos des de 1-1-1970.

// Exemplo dia atual mais 5 dias
let d = new Date();
d.setDate(d.getDate() + 5);
```