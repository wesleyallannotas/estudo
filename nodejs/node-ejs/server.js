const express = require('express');
const app = new express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  const items = [
    {
      title: 'Dicas do Node',
      message: 'Se mantenha atualziado aqui',
    },
    {
      title: 'Aprenda JS',
      message: 'Aprenda mais sobre a linguagem mais famosa',
    },
    {
      title: 'Impressora 3D',
      message: 'Os perigos da impressão de armas',
    },
  ];
  const subtitle = 'Pacote interessante para montagem rápida!';
  res.render('pages/index', {
    posts: items,
    subtitle: subtitle,
  });
});

app.get('/sobre', (req, res) => {
  res.render('pages/about');
});

app.listen(8080);
console.log('Rodando');
