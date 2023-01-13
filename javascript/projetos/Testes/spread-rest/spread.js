// Novas Arrays e Parâmetro
function sum(a, b, c=0, d=0, e=0) {
  return a + b + c + d + e;
}

const values = [5, 10, 15];          // 5, 10, 15
const values2 = [...values, 20];     // 5, 10, 15, 20
const values3 = [1, ...values, 20];  // 1, 5, 10, 15, 20

console.log(sum(...values));   // 30
console.log(sum(...values2));  // 50
console.log(sum(...values3));  // 51

// Junto com New
var dataField = [1970, 0, 1];
var d = new Date(...dataField);
console.log(d);

// Objetos
let obj1 = { foo: 'bar', x: 42 };
let obj2 = { foo: 'baz', y: 13 };
const clonedObj = { ...obj1 };            // { foo: "bar", x: 42 }
const mergedObj = { ...obj1, ...obj2 };  // { foo: "baz", x: 42, y: 13 }
console.log(clonedObj, mergedObj);

// Shallow Cloning
let obj3 = {
	foo: 'bar',
	x: 42,
	bar: 'foo',
	// Sub-objeto não será clonado e sim referenciado
	object: {
		subFoo: 'bar',
		subX: 42,
		subBar: 'foo'
	}
}

let obj4 = {...obj3}
obj4.foo = 'Mudei';
obj4.bar = 'Mudei também';
obj4.object.foo = 'Mudei';
obj4.object.bar = 'Mudei também';
console.log(obj3);
console.log(obj4);
