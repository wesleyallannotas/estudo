const readline = require('readline');

const terminal = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const questionAsync = question => new Promise((resolve, reject) => {
  terminal.question(`${question}\n`, resolve);
})

function questionAsyncAwait(question) {
  return new Promise((resolve, reject) => {
    terminal.question(`${question}\n`, msg => {
      !!msg ? resolve(msg) : reject(new Error('O campo não pode estar vazio!'))
    })
  })
};

// Callbacks
/*terminal.question('Seu nome?\n', (res1) => {
  terminal.question('Seu Idade?\n', (res2) => {
    console.log(`Ola ${res1}, Parabens pelos seus ${res2} anos de idade!`)
    terminal.close();
  })
})*/

// Promises
/*let name, age;
questionAsync('Seu nome?')
  .then(res => {
    if(!res) throw new Error('Campo Vazio!');
    name = res;
  })
  .then(() => questionAsync('Sua Idade?'))
  .then(res => {
    if(!res) throw Error('Campo Vazio!');
    age = res;
  })
  .then(() => console.log(`Ola ${name}, Parabens pelos seus ${age} anos de idade!`))
  .catch(err => console.log(err))
  .finally(() => terminal.close())*/

// Async/Await
async function main() {
  try {
    let name = await questionAsyncAwait('Seu nome?');
    let age = await questionAsyncAwait('Sua idade?');
    console.log(`Ola ${name}, Parabens pelos seus ${age} anos de idade!`);
  } catch(err) {
    console.log('Deu Ruim!', err.stack);
  } finally {
    terminal.close();
  }
};

main();