# # SEM BREAK

# valores = list()
# resp = ' '
# while resp not in 'N':
#     resp = ' '
#     valor = int(input('Digite um valor: '))
#     if valor in valores:
#         print('Valor dubliplicado! Nao vou adicionar..')
#     else:
#         print('Valor adicionado com sucesso!')
#         valores.append(valor)
#     resp = str(input('Que continuar? [S/N] ')).strip().upper()[0]
#     while resp not in 'SN':
#         resp = str(input('Resposta Invalida! Quer cotinuar? [S/N]: ')).strip().upper()[0]
# print('-='*35)
# # print(f'Vode digitou os valores {sorted(valores)}')
# valores.sort()
# print(f'Voce digitou os valores {valores}')

# COM BREAK

valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor dubliplicado! Nao vou adicionar..')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(valor)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta Invalida! Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*35)
valores.sort()
print(f'Voce digitou os valores {valores}')
