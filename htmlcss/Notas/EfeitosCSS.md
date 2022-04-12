# 📖 Degrade
É possivel criarmos degrade dentro do CSS utilizando a propriedade `linear-gradient()` como valor dentro da propriedade `background`

## 🤔 Como fazer
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
## 🧬 Compatibilidade
Para evitar problemas com verses antigas de navegadores podemos adicionar mais vezes a mesma linha pra garantir o funcionamento  
`-moz-linear-gradient()`: Corrigir incompatibilidade com versões do Mozilla  
`-o-linear-gradient()`: Corrigir incompatibilidade com versões do opera  
`-webkit-linear-gradient()`: Corrigir incompatibilidade com versões do safari

>Vale ressaltar que essa mesma forma de corrigir incompatibilidade funciona para outras ferramentas, vale a pena pesquisar
>

# Sombras

Possível adicionar sombras em texto e elementos através de CSS, segui por valores para eixoX, eixoY, Blur, Cor

## Sombras em elementos

Através da propriedade `box-shadow`.
```css
/* offset-x | offset-y | blur-radius | color */
box-shadow: 10px 5px 5px black;
```

## Sombra em texto

Funciona da mesma forma, porem mudando a propriedade para `text-shadow`
```css
/* offset-x | offset-y | blur-radius | color */
text-shadow: 10px 5px 5px black;
```

# Bordas Arredondadas

Através da propriedade `border-radius` podemos definir um valor para arredondar as bordas do elemento.
```css
div {
    border-radius: 10px
}
```

## Arredondar extremidade especifica

Possível especificar qual extremidade arredondar.
```css
div {
    border-top-left-radius: 10px;
    border-bottom-right-radius: 10px;
}
```