const getFlag = require('./module');

if (process.argv.indexOf('-h') !== -1) {
  console.log('comman [flag] value');
  return;
}

let arguments = {};
for (let argument of process.argv) {
  if (argument.search(/^--*/) !== -1) {
    arguments[argument.substring(2)] = argument;
  }
}

if (arguments.greeting !== undefined && arguments.name !== undefined) {
  console.log(
    `Ola ${getFlag(arguments.name)}. ${getFlag(
      arguments.greeting
    )}, Estou sempre a disposição!`
  );
}
