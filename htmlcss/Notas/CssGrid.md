# Introdução
Junto com o flexbox e utilizado para montar o layout da pagina.  
Assim como no flexbox e necessário um container onde dentro dele adicionaremos os items.

# Usando 
Basta ativar o grid no Display
```css
.container {
    display: grid;
  }
```
## Organizar
Regras gerais são aplicadas no container, já regras especificas são aplicadas no item especifico.

# Colunas
Geralmente se defini o grid inicialmente por colunas, depois fazemos as alterações em cima disto.  
```css
.container {
    /* 3 Colunas de 100px */
    grid-template-colums: 100px 100px  100px;
    /* 2 colunas que ocupa toda tela */
    grid-template-colums: auto auto;
  }
```

## grid-auto-columns
Define o tamanho das colunas do grid implícito (gerado automaticamente, quando algum elemento é posicionado em uma coluna que não foi definida).
```css
grid-auto-columns: 100px
/* As colunas implícitas, geradas automaticamente, terão 100px de largura.*/

grid-auto-colums: 50px 100px;
/*cria um padrao para a criacao de novas colunas implicita*/
```

# Linhas 
Funciona da mesma forma que as colunas porem com um pouco menos de controle pois não sabemos exatamente quantas linhas teremos, por isso geralmente definimos por colunas.
```css
.container {
    grid-template-rows: auto 200px 100px;
  }
```
> Pela logica coluna defini largura e linhas definem altura.

## grid-auto-rows
Define o tamanho das linhas do grid implícito (gerado automaticamente, quando algum elemento é posicionado em uma linha que não foi definida).
```css
grid-auto-rows: 100px
/* As linhas implícitas, geradas automaticamente, terão 100px de altura.*/

```
# grid-auto-flow
Define o fluxo dos itens no grid. Se eles vão automaticamente gerar novas linhas ou colunas.
```css
grid-auto-flow: row
/*Automaticamente gera novas linhas.*/

grid-auto-flow: column
/* Automaticamente gera novas colunas. */
```

# Gaps
Espaçamento entre os items, esse gap pode ser definido apenas em colunas ou linhas ou em ambos.
```css
.container {
    /* gaps especificos */
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    /* gaps simplificado */
    grid-gaps: 10px;
    grid-gaps: linha coluna;
  }
```
> Hoje em dia já não se utiliza o prefixo grid, assim sendo necessário apenas o uso do gap.
>

# Unidade FR
Unidade criada para o css grid, ela **representa fracão do espaço disponível do grid**, unidade totalmente flexível, considera o gapo.  
Respeita o conteúdo.

# Função Repeat
Basicamente repete o que colocar entre parenteses, primeiro valor sera quantos vezes quer repetir em seguida informa o que vai repetir
```css
grid-template-colums: repeat(3, 100px);
/* Mesma coisa que */
grid-template-colums: 100px 100px 100px;

grid-template-columns: repeat(3, 1tr) 200px;
/* Mesma coisa que */
grid-template-colums: 1tr 1tr 1tr 200px;

grid-template-colums: repeat(2, 100px 200px);
/* Mesma coisa que */
grid-templante-colums: 100px 200px 100px 200px;
```
## auto-fit e auto-fill
O `auto-fit` tenta preencher com o que tem de conteúdo.  
O `auto-fill` tenta preencher colunas independente se existem conteúdo ou não.

# Grid Auto
podemos definir auto para row ou colums dessa forma definindo um tamanho para todos.
```css
.container {
    grid-auto-rows: 200px;
    grid-auto-colums: 200px;
  }
```

# Função minmax
Através desta função podemos definir um valor minimo e máximo, assim criando um range de tamanho para os items.  
```css
.container {
    grid-auto-rown: minmax(50px, auto);

    grid-template-colums: repeat(4, mixmax(100px, 300px));
  }
```

# Posicionamento
Funciona a mesma forma de posicionamento do flexbox utilizando `justify-content`, `align-items` e `align-content`

# Mesclando Itens

## Mesclando colunas
Possível alterar o tamanho de um item específicos com as propriedades `grid-colum-star` e `grid-column-end` definindo em qual coluna este determinado item deve iniciar e terminar.
> Possível simplificar com a propriedade `grid-colum: start / end`
>

## Mesclando Linhas
Basicamente igual a coluna porem ele exige que seja definido um start e um end para colunas quando for mesclar em linha.
```css
.item1 {
    grid-colum-star: 1;
    grid-colum-end: 2;
    grid-row-star: 1;
    grid-row-end: 3;
  }
```
> Possível simplificar com a propriedade `grid-row: start / end`
>

## Span na mesclagem
Utilizando span nos referimos a quantidade que queremos que expanda.
```css
.item1 {
    grid-colum: 1 / span 2;
  }
```

# Grid Area
## Primeira forma de uso
Basicamente uma abreviação, em linha e coluna são atribuídos quatro valores, sendo a ordem  
1. `grid-row-star`
2. `grid-column-end`
3. `grid-row-end`
4. `grid-column-end` 
```css
.item1 {
    grid-area: 1 / 1 / 3 / 3;
  }
```

## Segunda forma de uso
Para nomear os items e ser possível chamá-lo pelo `grid-template-areas` 
```css
.item1 {
    grid-area: item1;
  }
.item2 {
    grid-area: item2;
  }
```

# Template Area
Montar o template através do `grid-template-areas` usando os nomes dados através do `grid-area`.
```css
.container {
    grid-template-area:
      "item1 item2"
      "item3 item3"
      "item4 ."
    ;
  }
```
> Ponto identifica um item vazio, necessário para funcionar.

# Responsividade
Basta re-ordenar dentro do media query
```css
@media (max-width:750px) {
    .container {
        grid-template-areas:
        "header"
        "menu"
        "content"
        "footer"
        :
      }
  }
```

# grid-template
Nada mais e do que um atalho para o template-area definindo de uma vez so, `grid-template-columns`, `grid-template-rows` e `grid-template-areas`
```css
/*A primeira linha com 50px, segunda com 150px e terceira com 100px. A primeira coluna com 100px, a segunda 1fr e a terceira com 50px.*/
.grid-template-1 {
	grid-template: 50px 1fr / 100px 1fr 100px;
}

.grid-template-2 {
	grid-template:
		"logo nav nav" 50px
		"sidenav content advert" 150px
		"sidenav footer footer" 100px
		/ 100px 1fr 50px;
}

```

# Grid
Atalho geral para definir o grid: grid-template-rows, grid-template-columns, grid-template-areas, grid-auto-rows, grid-auto-columns e grid-auto-flow

```css
grid: 100px / auto-flow 100px 50px
/* Gera uma linha com 100px de altura. O grid-auto-flow é definido como column (pois está logo antes da definição das colunas). Ele também define o grid-auto-columns com 100px 50px */
```

Link importante:
https://www.origamid.com/projetos/css-grid-layout-guia-completo/
