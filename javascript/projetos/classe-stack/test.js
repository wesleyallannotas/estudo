const Stack = require('./Stack');
// import Stack from './Stack';

const pilha = new Stack();

pilha.push('Entendendo Algoritmos');
process.stdout.write(pilha.peek() + '\n');
process.stdout.write(pilha.pop() + '\n');
