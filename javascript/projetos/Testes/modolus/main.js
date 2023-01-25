const Mat = require('./mat');
const readline = require('readline');

const terminal = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

terminal.question('Insira o primeiro valor\n', val1 => {
  terminal.question('Insira o segundo valor\n', val2 => {
    terminal.question('Insira o tipo de operação\n', type => {
      const result = Mat[type](Number(val1), Number(val2));
      console.log(`O resultado da operação de ${type} dentre ${val1} e ${val2} é ${result}`);
      terminal.close();
    })
  })
})