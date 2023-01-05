function a(func, string) {
    let e = ' foda-se';
    return (func(e) + string);
}

// Função anonima Arrow Funcion
// console.log(a((e) => {return 'José' + e;}, 'Manso'));

// Atalho de função
function b(e) {
    return ' José' + e;
} 

console.log(a(b, ' manso'))