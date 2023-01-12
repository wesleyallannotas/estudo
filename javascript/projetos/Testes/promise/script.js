let aceitar = true;

console.log('Pedir UBER');

const promessa = new Promise((resolve, reject) => {
  if (aceitar) {
    return resolve('Carro chegou!');
  } 
  return reject('Pedido Negado!');
});

promessa
  .then(result => console.log(result))
  .catch(erro => console.log(erro))
  .finally(() => console.log('Finalizada'));

console.log('Aguardando');
