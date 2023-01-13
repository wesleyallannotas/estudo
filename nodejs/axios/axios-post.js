// import axios from ('axios');
const axios = require('axios');

axios.post('/user', {
  firstNmae: 'Wesley',
  lastName: 'Silva'
})
.then( res => console.log(res))
.catch( err => console.log('Erro!\n', err));
