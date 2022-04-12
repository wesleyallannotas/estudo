# 🎨 Formas de definir Cor(Color):
Existem diversas formas de atribuir cor com CSS.

## Atribuindo por nome

Forma mais simples porem mais limitada, a forma que existe menos opções de cor
`color:red;`

## Atribuindo com RGB

RGB cada cor no caso, Red, Verde, Blue, atribuímos um valor entre 0 e 255.
`color:rgb(255, 255, 255);`
`color:rgba(...)` o ultimo equivale a transparência

## Atribuindo com código Hexadecimal

Código Hexadecimal (Letras e números) : {0,1 ... 8,9,a,b,c,d,f}
`color:#FF0000;`
 F = representa máximo da cor
#FFFFFF : Branco soma de todas as cores.
#FF0000 : Vermelho (Máximo de luz no vermelho)
#00FF00 : Verde  (Máximo de luz no Verde)
#0000FF : Azul  (Máximo de luz no azul)
Mixando as Cor primarias temos a paleta de cores.
#FFFF00 : Amarelo (Máximo de luz no vermelho e verde)
#FF00FF : Roxo (Máximo de luz no vermelho e azul)
#00FFFF : Ciano  (Máximo de luz no vende e azul)

## Atribuindo com hsl

Com o hsl usamos porcentagem (%)
`color: hsl(100%, 0, 0)`
No caso acima gerando um vermelho.

## Atribuindo com currentColor
Esta sendo mais utilizado ultimamente, através da herança ele pegou o `color` do seu elemento anterior(seu elemento pai):
```css
body {
    margin: 0;
    color: #ff0000;
}
h1 {
    border: 2px solid currentColor;
}
```
Assim herdara o vermelho(#ff0000) do body para o border do h1.