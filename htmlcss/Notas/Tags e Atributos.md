# Tags e Atributos.

Created Time: January 22, 2022 12:50 PM
Tags: 🏷 Tags, 📃 Texto, 🧬 HTML, 🧰 Atributos

HTML sua sigla significa *Hyper Text Markup Language*, ou seja, é uma linguagem de marcação de texto caracterizada pelo uso de TAGS, o HTML foi criado apenas para apresentar informações, isto é, sem dinamismo, exemplo e se quisermos fazer cálculos que variam de acordo com a entrada do usuário? Não podemos, pois o HTML no máximo será o responsável em exibir o resultado do cálculo, mas não realizá-lo.

## Funcionamento das Tags

Entre a abertura e o fechamento se encontra o conteúdo da tag.

`<>` = Abertura

`</>` : Fechamento da tag

## Existe elementos Vazios

Não tem conteúdo e sim atributos, ou seja, tudo dentro de apenas uma tag, fechando nela mesma.

Exemplo tag de imagem : `<img src="" alt=""/>`

## Atributos HTML

Sintaxe dos atributos `< atributo="valor" >` 

São sempre atribuídos na tag de abertura.

São dês de configurações a informações extras

Exemplo tag img  `<img src="" alt=""/>` (caso da imagem e configuração pura)

Configuração : `src=""` caminho da imagem, `alt=""` texto que aparece caso de problema de carregamento na imagem

## Atributos Booleanos

Não precisam de conteúdo

`<input type ="text" disable>`

`disable` atributo booleano (Verdadeiro ou falso)

## Atributos Globais mais utilizados

Atributos globais, são atributos aplicáveis a todas as tags

**class** = Serve para classificar, utilizamos para aplicar estilo CSS e também usamos para acessar no Javascript

**contenteditable** = Significa que pode editar o conteudo direto da pagina do site (Recebe true ou false, ou seja, booleano) quando salva a pagina perde a modificação

**data-*** = Pode colocar qualquer coisa onde esta o asterisco exemplo data-id

**hidden** = esconde uma tag

**id** = pode usar um id por pagina com aquele nome, não e igual classe que pode atribuir a mesma varias vezes.

**style** = ja aplica modificações CSS no html, e mais profissional criar um arquivo .css

**tabindex** = tab index cria uma navegação por tab na pagina seguindo a ordem que adicionar nele exemplo: <div tabindex ="1"> o primeiro tab ira nessa <div>

**title** = Atribui um titulo, não muda em termos visuais. aparece quando deixa o mouse diescansando em cima.

## Aninhamento de tags

Não podemos nos perder no aninhamento de tags.

**Exemplo de aninhamento errado:**

`<p> Vou <em>escrever<p> um parágrafo <em>`

Exemplo de aninhamento correto:

`<p> Vou <em>escrever<em> um parágrafo <p>`

O primeiro a abrir é o ultimo a fechar.

### Hierarquia das tags

```html
<div>
	<p>
		Vou <em>escrever um parágrafo</em>
	</p>
</div>
```

`<em>` e filha da tag `<p>` e a tag `<p>` e filha da tag `<div>` a tag `<div>` e a pai de todas as tag.

### Fluxo

Cada a tag e lida na ordem da escrita.

```html
<p>
	Vou <em>escrever um parágrafo</em>
</p>
<p>
	segundo paragrafo
</p>
```

Ou seja na pagina HTML ira aparecer um paragrafo, quebra de linha e outro paragrafo. e ira aparecer os paragrafo nas ordem escritas, primeiro aparece o primeiro escrito

### Posicionamento dos elementos

Por que o `<p>` quando finalizado e vai para outro, quebra linha em vez de continuar na frente, e o `<em>` não, basicamente pois `<p>` é um elemento em **block** e o `<em>` e um elemento em **inline**

## Conteúdo do texto e caracteres reservados.

O HTML ignora todos os espaços em brancos e quebras de linhas, que não foram feitos por tags.

Os caracteres reservados, são caracteres que a linguagem tem como importante ou seja não são simplesmente digita-los pois dará conflito, para digita-los por exemplo no HTML tem que escrever um código para ele interpretar e colocar como texto.

< = &lt;

< = &gt;

& = &amp;

"" = &quot;

'' = &apos;

---

`<h1>`,`<h2>`..`<h6>` : Tag de Titulos **(usa para hierarquizar os títulos, não usar para aumentar ou diminuir titulo, isso seria estilizar e estilar e com CSS)**

---

## Formatação de texto com HTML

`<i>` : Itálico

`<b>`  : Negrito

`<em>` : Itálico semântico (dar ênfase)

`<strong>` : Negrito semântico (palavra importante)

`<small>` : Diminui o tamanho do texto, diminui em relação ao padrão em volta dela, ou seja, se adapta de acordo aos outros textos.

`<del>` : Cria um risco em cima do texto.

`<mark>` : Imita uma marcação com marca texto. (adiciona um background amarelo)

`<sup>` : Pega o texto, diminui a fonte, e ira subir

`<sub>` : Mesmo que o sup porem em vez de subir, desce.

---

## Button

Tag para criar botões

`<botton>clique em min</botton>`

---

## Quebras de linha

`<br>` : Criar quebra de linha (br vem do break de quebra)

`<hr>` : Quebra linha, mas cria uma fina linha horizontal

## Criar Comentários

`<!— comentario —>`

## Declaração

`<!` : Declaração, não é tag