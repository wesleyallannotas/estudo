// import axios from 'axios';
const axios = require('axios');

Promise.all([
  axios.get('https://api.github.com/users/wesleyallan'),
  axios.get('https://api.github.com/users/wesleyallan/repos')
])
.then( responses => {
  console.log(responses[0].data.login);
  console.log(responses[1].data.length);
})
.catch( err => console.log(err.message));

async function getUserPosts(userName) {
  const api = `https://api.github.com/users/${userName}`

  const [user, repos] = await Promise.all([  // Apenas como exemplo
    axios.get(api),
    axios.get(api+`/repos`)
  ])

  console.log(user.data);
  console.log(repos.data);
}

// getUserPosts('wesleyallan');
