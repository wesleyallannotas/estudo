nota1 = float(input('Primeira nota do aulo: '))
nota2 = float(input('Segunda nota do aulo: '))
media = (nota1 + nota2) / 2

# f'String
print(f'A media entre {nota1} e {nota2} e igual a {media:.1f}')

# Método format
print('A media entre {} e {} e igual a {:.1f}'.format(nota1, nota2, media))