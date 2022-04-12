# Modelos

Criado uma `div` com `class` models, onde dentro dela possui os modelos que sera usados para se replicas com *JS*, um modelo para as cada item de pizza e um modelo para cada item do carrinho de compra.

# Listando Pizzas

Através do arquivo `pizzas.js` onde dentro se encontra um *JSON* das pizzas, sera usado esses dados para preencher o modelo de `pizza-item` e jogar na tela, assim sera feito com cada item, ou seja, cada sabor de pizza.  
`document.querySelector('.models .pizza-item').cloneNode(true);` - Seleciona a classe `pizza-item` dentro de `models`, usa a função `cloneNode` para clonar o HTML passa o parâmetro `true` para pegar o item e tudo que estiver dentro dele.  
Os clones serão jogados dentro da `div` que possui a class `pizza-area` através da função `append()`

# Criando modal (Tela de seleção quando escolher sabor)

Inicia adicionando um evento de click a tag `<a>`, onde junto desta função reinicia as informações padrões do Modal, e puxamos as informações de `pizzaJson` para preencher p modal.
```javascript
    pizzaItem.querySelector('a').addEventListener('click', (e)=>{
        e.preventDefault(); // Previda a ação padrão.
    })
```
Criado um efeito de opacidade com a junção de CSS e Javascript.
> O javascript e muito rápido, ou seja, para que ocorra e necessário criar a um timer mesmo que mínimo para mudar a opacidade de 0 para 1.
>
Criado uma variavel para guardar a informação de qual pizza se encontra no *Modal* `modalQt`  
> `forEach()` - Para cada um dos items.
>
função `closeModal()` criada para fechar o modal  
Através da variavel `modalKey` conseguimos o index da pizza selecionada para mandar as informações contidas no `pizzaJson`  