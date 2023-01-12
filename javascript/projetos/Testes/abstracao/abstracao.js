class Parafuso {
  constructor() {
    if (this.constructor === Parafuso) {
      // Caso tente instanciar parafuso
      throw new Error('Classe abstrata não pode ser instânciada');
    }
  }
  get tipo() {
    throw new Error('Método "get tipo()" precisa ser implementado');
  }
}

class Fenda extends Parafuso {
  constructor() {
    super();
  }
  get tipo() {
    return 'fenda';
  }
}

class Philips extends Parafuso {
  constructor() {
    super();
  }
  get tipo() {
    return 'philips';
  }
}

class Allen extends Parafuso {}

let fenda = new Fenda();
let philips = new Philips();
let allen = new Allen();

console.log(fenda);
console.log(philips);
console.log(allen);

console.log(fenda.tipo, philips.tipo);
console.group(allen.tipo);
