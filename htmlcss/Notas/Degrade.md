# 📖 Introdução
É possivel criarmos degrade dentro do CSS utilizando a propriedade `linear-gradient()` como valor dentro da propriedade `background`

# 🤔 Como fazer
Adiciona `linear-gradient()` dentro do `background`, onde em sequencia definimos:
1. Angulo do degrade (`deg`)
2. Primeira Cor
3. Segunda Cor
4. Quantas Cores desejarmos

```CSS
div {
    background:linear-gradient( 180deg, red, blue);
}
```
# 🧬 Compatibilidade
Para evitar problemas com verses antigas de navegadores podemos adicionar mais vezes a mesma linha pra garantir o funcionamento  
`-moz-linear-gradient()`: Corrigir incompatibilidade com versões do Mozilla  
`-o-linear-gradient()`: Corrigir incompatibilidade com versões do opera  
`-webkit-linear-gradient()`: Corrigir incompatibilidade com versões do safari

>Vale ressaltar que essa mesma forma de corrigir incompatibilidade funciona para outras ferramentas, vale a pena pesquisar
>