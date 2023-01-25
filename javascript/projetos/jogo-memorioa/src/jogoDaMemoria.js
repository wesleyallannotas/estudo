class JogoDaMemoria {
   // Desestruturação
  constructor({ tela }) {
    this.tela = tela;

    this.heroisIniciais = [
      { img: './assets/image/batman.png', name: 'batman' },
      { img: './assets/image/antMan.png', name: 'antman' },
      { img: './assets/image/hellBoy.png', name: 'hellboy' },
      { img: './assets/image/cyclops.png', name: 'cyclop' },
    ]
  }
  inicializar() {
    this.tela.atualizarImagens(this.heroisIniciais);
  }
}