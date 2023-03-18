lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for item in lista:
    print(f'\nNa palavra {item} temos ', end='')
    for i in range(0, len(item)):
        if item[i] in 'AEIOU':
            print(item[i].lower(), end=' ')
