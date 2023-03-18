def area(l, c):
    area = l * c
    print(f'A area de um terreno {l}x{c} e de {area}m2')


print('Controle de terrenos')
print('-' * 15)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
