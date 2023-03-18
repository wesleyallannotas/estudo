# Protegendo caracteres ( ’’ “” \ )

Tags: #️⃣ Comandos, 🔣 Aspas

# Introdução

Existe uma serie de caracteres especiais entre ele temos por exemplo o cifrão $, que dentro do shell tem como papel referenciar uma variável, porem como o protegemos para ele perder essa função e se tornar um carácter comum, neste caso usaremos a aspas ficando `‘$'`

## Protegendo carácter

`“*”` - Protege os caracteres exceto $ ` /

`‘*’` - Protege TODOS que estão dentro 

`\*` - Protege apenas o próximo carácter