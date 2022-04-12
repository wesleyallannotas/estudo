# 📖 Introdução
Através das tag de *Social Sharing* podemos criar uma formatação que sera exibida caso o link do nosso site seja compartilhado em plataformas que cria aquela especia de *card* exibindo uma imagens sobre o site o que tem nele, como se fosse uma apresentação

> 💡 Por exemplo quando compartilhamos um link no WhatsApp
>

Para que seja possível exibir esses cards nos aplicativos do facebook e necessário acessar uma das ferramentas de desenvolvedores deles [Sharing Debugger](https://developers.facebook.com/tools/debug/?locale=pt_BR) através dela *linkamos* o site e sera criado um cache no servidores deles

> ⚠️ **Caso alterarmos algo sera necessário passar o site pela ferramenta novamente para alterara**
>

# ✍ Criando o Social Sharing
E criado através das *tags* `<meta>` dentro do `<head>` do nosso documento *HTML*  
A *tag* sera criada da seguinte forma `<meta property="" content=""/>`  
Dentro do atributo *property* informaremos o que é  
Dentro do atributo *content* o conteúdo  
Sendo necessário que adicionamos as seguintes informações:
- **Link** - Mesmo possuindo nossa URL, é pedido um *link*
`<meta property="og:url" content="http://linkdosite.com"/>`
- **Tipo** - Informa o tipo do site, existe infinitas opções, para Artigos(article) Vendas(product) Site Pessoal (website)  
`<meta property="og:type" content="website"/>`
- **Titulo** - Titulo que sera exibido quando compartilhado o link  
`<meta property="og:title" content="Titulo de Exemplo"/>`
- **Descrição** - Texto que aparecera embaixo do titulo, breve explicação  
`<meta property="og:description" content="Descrição de Exemplo sobre o website"/>`
- **Imagem** - Pode ser incluída uma imagem.  
`<meta property="og:image" content="linkdaimagem"/>`
- **Outros** - E possível acessar o [Doc do facebook](https://developers.facebook.com/docs/sharing/webmasters/) para ver todas as tags possíveis.

>⚠️ Não importa a ordem que seja adicionado
>