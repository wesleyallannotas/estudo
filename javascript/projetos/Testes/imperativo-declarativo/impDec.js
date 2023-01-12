// Imperativo
let resultado = [];
function dobrar(array) {
  for (let i = 0; i < array.length; i++) {
    resultado.push(array[i] * 2);
  }
  return resultado;
}

dobrar([1, 2, 3, 4, 5]);

console.log('---Imperativo---');
console.log(resultado);

// Declarativo
console.log('---Declarativo---');
const dobrarDec = array => array.map(item => item * 2);
console.log(dobrarDec([1, 2, 3, 4, 5]));
