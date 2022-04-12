# Estrutura e Semântica Básica

Created Time: January 22, 2022 12:50 PM
Tags: 📑 Estrutura, 🔎 Semântica, 🧬 HTML

## Base:

No VScode utilizando o atalho ! Emmet que ele criara uma base de HTML pronta.

```html
<!DOCTYPE html> <!-- identificar que estamos trabalhando com HTML5 -->
<html lang="pt-br">
	<head> <!-- Conteúdo complementar/configurações -->
		<title> Titulo da pagina </title>
		<meta tags>
		<link oara arquivos externos>
	</head>
	<body> <!-- Conteúdo da pagina -->
		<h1> titulo da pagina</h1>
		<p>texto</p>
		<ul>
			<li>item de lista</li>
		</ul>
	</body>
</html>
```

## Dentro das estruturas base

`<html>`: Tag pai de todas pela logica da hierarquia, elemento root, a raiz, inicio da cadeia, uma boa pratica e colocar um atributo da linguagem da pagina `<html lang="pt-br"`

`<head>`: Elemento irmão do `<body>`, filho do `<html>`, contem configurações importantes para pagina, Informações complementares que não fazem parte do conteúdo visual da pagina, por aqui adicionamos o titulo que fica na aba do navegador por exemplo.

`<body>`: Elemento irmão do `<head>`, todo o conteúdo visível da pagina

## Doctype

Não é html puro, é uma forma de informar para o browser que tipo de documento estou escrevendo

Sempre na primeira linha, inicio do documento.

`<!` : Declaração, não é tag

Informar HTML5: `<!doctype html>`

## Meta Tag

Atribui meta dados a pagina, são adicionados no `<head>`.

O Chrome, a partir da versão 55, passou a detectar automaticamente o *encoding* dos arquivos. Então, é possível pensar que não é mais necessária a tag `<meta charset="UTF-8">`.

No entanto, ela deve continuar a ser usada, porque nem todos os navegadores detectam o *encoding* automaticamente, sendo assim, é uma boa prática manter a tag `<meta>` indicando o `charset` usado na hora de criar o arquivo.

`<meta charset="utf-8">` indico para o browser que essa pagina tem um tipo de codificação de carácter UTF-8 Codificação mais usada, Abrange vários tipos de caractere, como c de cedilha, acentuação

`<meta name="author" content="nomedoautordosite">` : informar o autor do site

`<meta name="descriptiom" content="descri do que vai encontrar">`

---

## Semântica

Escrever um site com o uso da semântica correta, facilita a localização por sites de busca como o google, ajuda leitores com dificuldade visual pois o programa de acessibilidade entendera o funcionamento do site, extremamente importante o uso da semântica correta.

### Cabeçalhos e parágrafos.

Usamos para estruturar o texto e não ficar uma bola de mistura de parágrafos e títulos

É uma boa pratica usar apenas um `<h1>` por pagina, pois se entende que se for necessário usar mais um `<h1>` esse conteúdo devia estar em outra pagina.

do `<h1>` ate o `<h6>` se trabalha com a ideia de níveis de títulos e subtítulos.

Usamos a tag `<p>` para dividir em parágrafos do nosso texto.

Normalmente se usa no máximo ate o `<h3>`.

### Listas

Podemos ter listas ordenas e não ordenadas, sempre colocamos nossa `<li>`dentre de `<ol>`(lista ordenada) ou `<ul`(lista não ordenada) sempre manter dentre de umas dessa tags, reforçando que HTML precisa ser semântico. 

### Citações

Usamos para identificar que estamos pegando texto de fora, dando os créditos ai criados original do conteúdo.

`<blockquote>`: Citar alguma coisa e quer deixar bem grande o que a pessoa falou.

Exemplo de uso:

```html
<blockquote cite="https://developer.mozilla.org/en-US/dpcs/Web/HTML/Element.blockquote">
	<p>O <strong>Elemento HTML <code>&al;blockquote&gt;</code></strong> (ou <em>HTML Block Quotation Element</em> indica que um texto externo foi citado.
	</p>
<blockquote>
```

Tag `<blockquote>` com atributo `cite=""` que serve para citar de qual Url tiramos essa citação, ou seja, dar os creditos.

`<cite>`: Citamos porem sem alteração visual, usamos para o fortalecimento da semântica e facilitar a acessibilidade.

Exemplo de uso:

```html
<p>De acordo com <a href="https://developer.mozilla.org/en-US/dpcs/Web/HTML/Element.blockquote">
	<cite>Página MDN Blockquite</cite></a>
</p>
```

`<p>`: Usando citação no paragrafo, iremos atribuir um cite a ele.

Exemplo de uso:

```html
<p cite="https://developer.mozilla.org/en-US/dpcs/Web/HTML/Element.blockquote">Usado para citações curtas que não precisam de parágrados ou quebras de linhas.</p>
```