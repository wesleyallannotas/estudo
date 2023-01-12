function roda(fn) {
  console.log('Dentro da função');
  fn();
}

roda(() => console.log('Teste'));
console.log('Fora');
