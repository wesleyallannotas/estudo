function retornaDois(value) {
  return [value, value * 2];
}

let vetor = retornaDois(2);
let [val1, val2] = retornaDois(2);

console.log(vetor);
console.log(val1);
console.log(val2);
