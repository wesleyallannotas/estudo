# Introdução

Semelhante ao `if`, porem existem situações que e preferível o uso dele.  
Usamos switch quando temos um valor especifico e precisamos a partir deste valor fazer varias condicionais diferentes.

# Sintaxe
Lembra o `case` em *shellscript* 

```javascript
let dia = 3;

switch(dia) {
    case 1:
        diaNome = 'Domingo';
        break;
    case 2:
        diaNome = 'Segunda-feira';
        break;
    case 3:
        diaNome = 'Terça-feira';
        break;
    case 4:
        diaNome = 'Quarta-feira';
        break;
    case 5:
        diaNome = 'Quinta-feira';
        break;
    case 6:
        diaNome = 'Sexta-feira';
        break;
    case 7:
        diaNome = 'Sábado';
        break;
}

switch(dia) {
    case 6:
    case 7:
        diaNome = 'Final de Semana';
        break;
    default:
        diaNome = 'Dia Util';
        break;
}
```

# `default`
Funciona como o asterisco m *shellscript* funcionando como a resposta padrão que sera enviada caso nao atenda nenhuma das condições