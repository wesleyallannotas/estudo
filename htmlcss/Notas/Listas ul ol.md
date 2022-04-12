# Listas <ul> <ol>

Created Time: January 22, 2022 12:50 PM
Tags: 📄 Lista, 🖌 CSS, 🧬 HTML

## Listas

### Não ordenadas (Simplesmente elencar item)

`<ul>` : lista não ordenada

`<li>` : item de lista (Não pode ter outro comando dentro de lista)

Estrutura:

```html
<ul>
	<li>...</li>
	<li>...</li>
	<li>...</li>
</ul>
```

### Ordenadas (Lista precisa obedecer uma ordem)

`<ol>` : Lista Ordenada

`<li>` : item da lista (Não pode ter outro comando dentro de lista)

Estrutura:

```html
<ol>
	<li>...</li>
	<li>...</li>
	<li>...</li>
</ol>
```

---

# List-Syle (CSS)

Listas já possui uma formatação padrão.

O list-style e uma forma de alterar essa formatação padrão.

```html
<!--Atravez do HTML usando atributos-->
<ol type="I"> <!--upper-roman ou seja algarismo romano maiusculo-->
	<li>...</li>
</ol>

<ol start="45"> <!--Deixa de começar apartir do 1 e sim do 45-->
	<li>...</li>
</ol>
```

```css
/*Atravez do CSS*/
li{                         
	list-style-type           /*Tipo do marcador da lista*/
	list-style-position       /*Posição da lista*/
	list-style-image          /**/
}
```

`type: none;` : Nenhum marcador de lista.

### Type para <ul>

`disc` : Ponto sólido (padrão)

`circle` : Circulo vazio

**`square`** : Quadrado vazio

---

### Type para <ol>

**`decimal` :** números decimas, iniciando com 1

HTML : `<ol type="1">`

**`decimal-leading-zero` :** Números decimais com zeros iniciais à esquerda (01, 02, 03, ..., 98, 99)

`lower-roman` : Números romanos minúsculos (i, ii, iii, iv, v, etc.).

HTML : `<ol type="i">`

**`upper-roman` :** números romanos maiúsculos (I, II, III, IV, V, etc.)

HTML : `<ol type="I">`

**`georgian` : N**umeração georgeana tradicional (an, ban, gan, ..., he, tan, in, in-an, ...)

**`armenian` : N**umeração armênia tradicional

**`lower-latin | lower-alpha` : L**etras ascii minúsculas (a, b, c, ... z)

HTML : `<ol type="a">`

**`upper-latin | upper-alpha` : L**etras ascii maiúsculas (A, B, C, ... Z)

HTML : `<ol type="A">`

**`lower-greek` :** caracteres gregos clássicos alpha, beta, gama (α, β, γ, …)

---

### Atributo start para definir de que contagem se inicia.

`<ol start="45">` Defini como inicio da contagem da lista o 45 e não o 1 que é o padrão.

---

## Nested list (lista dentro de lista)

Podemos adicionar quantas listas dentro de listas quisermos.

```html
<ul>
	<li>Café</li>
	<li>
	Chá
	<ul>
		<li>Chá Preto</li>
		<li>Chá Verde</li>
	</ul>
	</li>
	<li>Leite</li>
</ul>
```