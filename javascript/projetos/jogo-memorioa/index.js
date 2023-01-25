function onLoad() {
  const dependecias = {
    tela: Tela
  }
  const jogodaMemoria = new JogoDaMemoria(dependecias);
  jogodaMemoria.inicializar();
};

window.onload = onLoad;