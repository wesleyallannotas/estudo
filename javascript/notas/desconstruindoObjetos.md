# Introdução

Recurso adicionado com o ECMAScript 6, alguns lugares chama *desestruturação*, funciona com *Objetos* e *Arrays*, nada mais e do que selecionar itens específicos e jogar dentro de variáveis, com cada item se alocando dentro de uma variavel diferente.
> Adicionando dois pontos ":" depois do nome do item, podemos escolher o nome da variavel criada que ira conter o valor daquele item
> Caso o item nao exista dentro do objeto, possível atribuir um valor a ele dentro da desconstrução, apenas adicionando um igual com o valor na frente, mas caso aja ou seja adicionado posteriormente o item ao objeto, ele pegara o valor do item no objeto.

# Sintaxe

```javascript
// Base
let {item, item...} = objetodesconstruir;
// Renomeando
let {item:renome, item...} = objetodesconstruir;
// Objeto dentro de objeto
let {itemObjeto:{item}, item...} = objetodesconstruir;
```

# Exemplo

```javascript
let pessoa = {
    nome: 'Wesley',
    sobrenome: 'Silva',
    idade: 23,
    social:{
        facebook: 'Wesley Silva',
        instagram: {
            url: '@wesleyallansilva',
            seguidores: 200;
        },
        twitter: 'Wesley_AllanS'
    },
    nomeCompleto: function() {
        return `${this.name} ${this.sobrenome}`;
    }
};
// Desconstruindo
let {nome:pessoaNome, sobrenome, idade, horasLivres = 8} = pessoa;
// Desconstruindo Objeto dentro de Objeto em linha.
let {nome, social:{instagram:{url:instagram}}} = pessoa // Objeto social dentro de pessoa, objeto instagram dentro de social, renomeio item url para instagram.
// Forma mais simples, de desconstruir objeto dentro de objeto.
let {facebook, instagram, twitter} = pessoa.social

console.log(pessoaNome, sobrenome, idade, horasLivres, instagram);
```

# Utilizando Desconstrução com Função

```javascript
let pessoa = {
    nome: 'Wesley',
    sobrenome: 'Silva',
    idade: 23,
    social:{
        facebook: 'Wesley Silva',
        instagram: {
            url: '@wesleyallansilva',
            seguidores: 200;
        },
        twitter: 'Wesley_AllanS'
    }
};

function dados({nome, sobrenome, social:{instagram:{url:instagram}}}) {
    return `${nome} ${sobrenome} (Siga em ${instagram}`;
}

console.log(dados(pessoa));
```