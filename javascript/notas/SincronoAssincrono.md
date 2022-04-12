# Diferença

Código Síncrono, e executado **linha a linha**, ou seja, so vai para a proxima linha quando o atual for finalizada a execução.
```javascript
// Código Síncrono
let nome = 'Wesley';
let sobrenome = 'Silva';
let completo = nome+" "+sobrenome;
```
Código Assíncrono, passa **para proxima linha sem que a execução da linha atual esteja finalizada**, ou seja, nao para o código para esperar uma execução ele segui enquanto deixa em execução
```javascript
// Código Assíncrono
let nome = 'Wesley';
let sobrenome = 'Silva';
let temperatura = Maquina.pegarTemp(); // Assíncrona
let completo = nome+" "+sobrenome;
```
> Toda requisição interna e assíncrona!