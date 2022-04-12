# Introdução

Novidades do ECMAScript 6, funções muito utilizadas hoje em dia

# Includes

Para *Array* e *Objeto*, ele **busca** por um **item** que quisermos **retornando um Boolean**, diferente de outras formas de busca que retorna posição do Item ou caso nao aja retorna -1
```javascript
let lista = ['ovo', 'carne', 'arroz'];

console.log(lista.includes('ovo'));
// resultado: true;
```
Para *Strings* ele **busca** se o **Carácter** existe ou nao, e **retornando um Boolean**, diferente de outros formas de busca que retorna a posição do Carácter ou caso nao aja retorna -1
> Vale lembra que Javascript e *Case Sensitive*, ou seja, carácter minúsculos e maiúsculo da mesma letra e tratado como diferente.
```javascript
let nome = 'Wesley';

console.log(nome.includes('E'));
// resultado: false;
```

# Repeat

Usado diretamente na *String* ou em uma variavel que contem uma *string*, utilizado para **repetir**
```javascript
let nome = 'Wesley';

console.log(nome.repeat(3));
// resultado: WesleyWesleyWesley

console.log('tes'.repeat(3));
//resultado: testestes
```