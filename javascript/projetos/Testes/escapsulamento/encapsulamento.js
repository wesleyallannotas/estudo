class Poligono {
  constructor(largura, altura) {
    this.largura = largura;
    this.altura = altura;
  }
  get area() {
    return this.#calcularArea();
  }

  #calcularArea() {
    return this.largura * this.altura;
  }
}

let poligono = new Poligono(50, 50);
console.log(poligono);
console.log(poligono.area);
poligono.largura = 60;
console.log(poligono);
console.log(poligono.area);
