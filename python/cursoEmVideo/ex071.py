print('='*35)
print(f'{"BANCO CEV":^35}')
print('='*35)
valor = int(input('Que valor voce quer sacar? R$'))
# # Logica Inicial
# nt1 = nt10 = nt20 = nt50 = 0
# while valor > 0:
#     if valor >= 50:
#         valor -= 50
#         nt50 += 1
#     elif valor >= 20:
#         valor -= 20
#         nt20 += 1
#     elif valor >= 10:
#         valor -= 10
#         nt10 += 1
#     else:
#         valor -= 1
#         nt1 += 1
# if nt50 > 0:
#     print(f'Total de {nt50} cedulas de R$50')
# if nt20 > 0:
#     print(f'Total de {nt20} cedulaas de R$20')
# if nt10 > 0:
#     print(f'Total de {nt10} cedulas de R$10')
# if nt1 > 0:
#     print(f'Total de {nt1} celulas de R$!')

# Logica Sofisticada
total = valor
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cedulasa de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
