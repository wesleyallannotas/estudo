const express = require('express');

const app = new express();

app.get('/', (req, res, next) => {
  res.locals.hello = 'Hello World';
  next();
});

app.get('/', (req, res) => {
  return res.send(res.locals.hello);
});

app.get('/', (req, res) => {
  res.send('Eu nunca serei chamado!')
})

app.listen('3000');
