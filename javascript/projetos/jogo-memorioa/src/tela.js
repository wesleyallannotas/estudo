const util = Util;

const ID_CONTEUDO = 'conteudo';
const ID_BTN_JOGAR = 'jogar';
const ID_MENSAGEM = 'mensagem';
const CLASSE_INVISIVEL = 'invisible';
const ID_CARREGANDO = 'carregando'; 
const ID_CONTADOR = 'contador';
const ID_BTN_MOSTRAR_TUDO = 'mostraTudo';
const MENSAGEM = {
  sucesso: {
    texto: 'Combinaçào correta!',
    classe: 'alert-success'
  },
  erro: {
    texto: 'Combinação incoreta!',
    classe: 'alert-danger'
  }
};
class Tela {
  static obterCodigoHmtl(item) {
    return `
    <div class="col-md-3">
      <div class="card" style="width: 50%;" onclick="window.verificarSelecao('${item.id}','${item.nome}')">
        <img src="${item.img}" name="${item.nome}" class="card-img-top"/>
      </div>
      <br />
    </div>
    `;
  }
  static configurarBotaoVerificarSelecao(funcaoOnClick) {
    window.verificarSelecao = funcaoOnClick;
  }
  static alterarConteudoHtml(codigoHtml) {
    const conteudo = document.getElementById(ID_CONTEUDO);
    conteudo.innerHTML = codigoHtml;
  }
  static gerarStringHtmlPelaImagem(itens) {
    return itens.map(Tela.obterCodigoHmtl).join('');
  }
  static atualizarImagens(itens) {
    const codigoHtml = Tela.gerarStringHtmlPelaImagem(itens);
    Tela.alterarConteudoHtml(codigoHtml);
  }
  static configurarBotaoJogar(funcaoOnClick) {
    const btnJogar = document.getElementById(ID_BTN_JOGAR);
    btnJogar.onclick = funcaoOnClick;
  }
  static exibirHerois(nomeDoHeroi, img) {
    const elementosHtml = document.getElementsByName(nomeDoHeroi);
    elementosHtml.forEach( item => (item.src = img));
  }
  static async exibirMensagem(sucesso = true) {
    const elemento = document.getElementById(ID_MENSAGEM);
    if(sucesso) {
      elemento.classList.remove(MENSAGEM.erro.classe);
      elemento.classList.add(MENSAGEM.sucesso.classe);
      elemento.innerText = MENSAGEM.sucesso.texto;
    } else {
      elemento.classList.remove(MENSAGEM.sucesso.classe);
      elemento.classList.add(MENSAGEM.erro.classe);
      elemento.innerText = MENSAGEM.erro.texto;
    }
    elemento.classList.remove(CLASSE_INVISIVEL);
    await util.timeout(1000)
      elemento.classList.add(CLASSE_INVISIVEL);
  }
  static exibirCarregando(mostra = true) {
    const carregando = document.getElementById(ID_CARREGANDO);
    if(mostra) {
      carregando.classList.remove(CLASSE_INVISIVEL);
      return;
    }
    carregando.classList.add(CLASSE_INVISIVEL);
  }
  static iniciarContador() {
    let contarAte = 3;
    const elementoContador = document.getElementById(ID_CONTADOR);
    const identificadorNoTexto = "$$contador";
    const textoPadrao = `Começando em ${identificadorNoTexto} segundo...`;
    const atualizarTexto = () => (elementoContador.innerHTML = textoPadrao.replace(identificadorNoTexto, contarAte--));
    atualizarTexto();
    const idDoIntervalo = setInterval(atualizarTexto, 1000);
    return idDoIntervalo;
  }
  static limparContador(idDoIntervalo) {
    clearInterval(idDoIntervalo);
    document.getElementById(ID_CONTADOR).innerHTML = "";
  }
  static configurarBotaoMostraTudo(funcaoOnClick) {
    const btnMostrarTudo = document.getElementById(ID_BTN_MOSTRAR_TUDO);
    btnMostrarTudo.onclick = funcaoOnClick;
  }
}
