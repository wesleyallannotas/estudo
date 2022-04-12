# Introdução

Quando voce faz uma requisição ira receber como resultado um *JSON* "puro", em forma de *string* onde dentro de encontra um *JSON*.
> Podemos que para envio de informação se faz no formato de *strings* onde para utilizado  necessário converter para *JSON* no formato padrão, ou seja, object.
```javascript
// Sintaxe JSON em forma de *String*
'{"nome": "Wesley","sobrenome": "Silva","idade": 23}'
```
Chamando o objeto `JSON` temos acesso a varias funções para manipular *JSONs*

# `JSON.parse()`

Como propriedade podemos atribuir um *JSON* "puro", em forma de *string*, e a função `parse()` pegara essa *string*  de *JSON* e transformar em um *JSON* real, ou seja, em formato de objeto.
```javascript
JSON.parse('{"nome": "Wesley","sobrenome": "Silva","idade": 23}');
// resultado: object {nome: 'Wesley',sobrenome: 'Silva',idade: 23}
```

# `JSON.stringify()`

**Inverso da função `parse()`**, ou seja, recebe um *JSON* em forma de objeto, e o transform em *JSON* em forma de *string*
```javascript
JSON.stringify({nome: 'Wesley',sobrenome: 'Silva',idade: 23});
// resultado: String '{"nome": "Wesley","sobrenome": "Silva","idade": 23}'
```