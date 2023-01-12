const Queue = require('./Queue');

const fila = new Queue();

fila.enqueue('teste');
console.log(fila);
console.log(fila.dequeue());
console.log(fila);
