let a = '1';
let b = '1a';
let c = 4 / []; // Infinity

console.log(isFinite(a));
console.log(isFinite(c));

console.log(isNaN(Number(a)));
console.log(isNaN(Number(b)));