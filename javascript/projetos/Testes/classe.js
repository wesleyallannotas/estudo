class Person {
  constructor(nome, peso, altura) {
    this.nome = nome;
    this.peso = peso;
    this.altura = altura;
  };

  #calculaImc() {
    return (this.peso / this.altura ** 2).toFixed(2);
  };

  get imc() {
    return `O Imc de ${this.nome} é ${this.#calculaImc()}`;
  };
};

const wesley = new Person('Wesley', 120, 1.90);

console.log(wesley.imc);  
wesley.#calculaImc();  // Propriedade não acessivel, método privado