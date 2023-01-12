import axios from 'axios';
// const axios = require('axios');

Promise.all([
  axios.get('https://api.github.com/users/wesleyallan'),
  axios.get('https://api.github.com/users/wesleyallan/repos')
])
.then( responses => {
  console.log(responses[0].data.login);
});
