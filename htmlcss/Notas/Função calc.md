# Função calc

Created Time: January 22, 2022 12:50 PM
Tags: 🖌 CSS

## Introdução

Função que permite fazer cálculos, por exemplo um calculo com base no tamanho da tela do usuário para redefinir o tamanho de uma div.

### Exemplo:

Redimensionar uma div para que tenha um espaçamento dos cantos da tela, sem usar margin(pois queremos testar o calc, apenas para aprendizado)

### CSS da Pagina base

```css
body {
  margin: 0;
}
.container {
  width: 100%;
  height: 200px;
  background-color: #ccc;
}
```

### Usando a função calc.

Assim a div pegara 100% de largura disponível e iniciara um calculo tirando 20px desse total, e por ser porcentagem, ele diminui e aumento em relação ao espaço de tela, independente de aumentar ou diminuir a tela o css calculara menos 20px.

```css
body {
  margin: 0;
}
.container {
  width: calc(100% - 20px);
  height: 200px;
  background-color: #ccc;
}
```