# Links <a>

Created Time: January 22, 2022 12:50 PM
Tags: 🔗 Link, 🖌 CSS, 🧬 HTML

## Links

`<a>` : Tag de link Precisa de atribuição, "a" vem de anchor de ancora

```html
<p> saiba mais sobre <a>HTML5</a> visitando nosso blog seja feliz </p>
```

**Exemplo abrir pagina em outra aba:**

```html
<p> 
saiba mais sobre <a href="http://www...com.br"target="_blank">HTML5</a> visitando
nosso blog seja feliz 
</p>
```

Não precisa ser apenas um texto, podemos colocar imagens ate uma div dentro onde será possível clicar e levara para outro link, pagina, seção entre outros.

`title="titulodolink"` Quando colocar o mouse em cima aparece o titulo em uma caixinha.

`target="_blank"` : Dizendo que quero que abra em outra aba. ( o target e uma nova pagina em branco para abrir o link)

**`<a href="#">` :** Cria um link falso, apenas com a aparência do link

**`<a href="http://www...com.br">` :** Vou para um link externo fora do meu site

**`<a href="outrapagina.html">` :**  Paginas entre meu próprio site

**`<a href="#secao">` :** Link de seção (Navegar na mesma pagina)

**`<a href="mailto:alguem@server.com">` :** Link de Email (não se usa geralmente pois necessita que o usuário tenha um software de gerenciar emails instalado)=

---

# Pseudo Classes em Links (CSS)

### Sintaxe:

```css
a:link { ... }        /*Link intacto, sem ter visitado, sem mouse sobre ele*/
	a:visited { ... }   /*Quando o link ja foi visitado*/
		a:hover { ... }   /*quando pasar o mouse sobre o link*/
			a:active { ... } /*Quando o lick estiver pressionado*/
```

Caso  tag `<a>` tenha uma classe, também podemos chamar no CSS pela classe `.link:hover` , primeiro aplicara as formatações feitas no link padrão, depois só ira alterar o que estiver dentro das pseudo classes, ou seja, caso na formatação base seja 30px de font com cor preta e na houver só atribuirmos cor azul, só ira mudar a cor, os 30px antes atribuídos se manterá.