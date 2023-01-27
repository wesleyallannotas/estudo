function onLoad() {
  const dependecias = {
    tela: Tela,
    util: Util
  };

  const jogodaMemoria = new JogoDaMemoria(dependecias);
  jogodaMemoria.inicializar();
}

window.onload = onLoad;
