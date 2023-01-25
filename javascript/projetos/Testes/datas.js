const hoje = new Date();

const diaSemana = hoje.getDay();
console.log(diaSemana);

const dia = hoje.getDate();
console.log(dia)
hoje.setDate(dia + 1);
console.log(hoje);

const ano = hoje.getFullYear();
console.log(ano);
hoje.setFullYear(ano + 1, 5, 29);
console.log(hoje);

const mes = hoje.getMonth();
console.log(mes);
hoje.setMonth(mes + 1, 24);
console.log(hoje);

const horario = hoje.getHours();
console.log(horario);
hoje.setHours(horario + 1, 35, 25, 780);
console.log(hoje);

const minutos = hoje.getMinutes()
console.log(minutos);
hoje.setMinutes(minutos + 1, 26, 781);
console.log(hoje);

const segundos = hoje.getSeconds();
console.log(segundos);
hoje.setSeconds(segundos + 1, 600);
console.log(hoje);

const milisegundos = hoje.getMilliseconds();
console.log(milisegundos);
hoje.setMilliseconds(milisegundos + 1);
console.log(hoje);

const wesley = new Date(1998, 5, 29);
const andressa = new Date(1991, 10, 24);

console.log(wesley > andressa);
// Nada impedete fazer direto, pois a instancia retorna o objeto da mesma forma.
console.log(new Date(1998, 5, 29) > new Date(1991, 10, 24));