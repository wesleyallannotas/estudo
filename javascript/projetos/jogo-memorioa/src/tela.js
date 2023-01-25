const ID_CONTEUDO = 'conteudo';
class Tela {
  static obterCodigoHmtl(item) {
    return `
    <div class="col-md-3">
      <div class="card" style="width: 50%;">
        <img src="${item.img}" name="${item.nome}" class="card-img-top"/>
      </div>
      <br />
    </div>
    `
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
}