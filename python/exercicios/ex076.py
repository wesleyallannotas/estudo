lista = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 
         'Estojo', 25.0, 'Transferidor', 4.20, 'Compasso', 9.20, 
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*45)
print(f'{"LISTAGEM DE PRECOS":^45}')
print('-'*45)
# Simplificado
for item in range(0, len(lista), 2):
    print(f'{lista[item]:.<35}R$ {(lista[item+1]):>7.2f}')
# # Par ou impar
# for item in range(0, len(lista)):
#     if item % 2 == 0:
#         print(f'{lista[item]:.<35}', end='')
#     else:
#         print(f'R$ {lista[item]:>7.2f}')
