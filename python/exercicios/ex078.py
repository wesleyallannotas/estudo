# Usando Max() e Min()

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e é na posiçao  ', end='')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}... ', end='')
    if pos == len(valores) - 1:
        print(f'Fim')
print(f'O menor valor digitado foi {min(valores)} e á na posiçao ', end='')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}...', end='')
    if pos == len(valores) - 1:
        print(f'Fim')

# # Usando loops e condicionais
#
# valores = list()
# menorValor = 0
# maiorValor = 0
# for c in range(0, 5):
#     valores. append(int(input(f'Digite um valor para a posicao {c}: ')))
#     if c == 0:
#         menorValor = valores[c]
#         maiorValor = valores[c]
#     else:
#         if menorValor > valores[c]:
#             menorValor = valores[c]
#         elif maiorValor < valores[c]:
#             maiorValor = valores[c]
# print(f'Voce digiotu os valores {valores}')
# print(f'O maior valor digitado foi {maiorValor} e na posicao ', end='')
# for pos, valor in enumerate(valores):
#     if valor == maiorValor:
#         print(f'{pos}...', end='')
#     if pos == len(valores) - 1:
#         print(f'Fim')
# print(f'O menor valor digitado foi {menorValor} e na posicao ', end='')
# for pos, valor in enumerate(valores):
#     if valor == menorValor:
#         print(f'{pos}...', end='')
#     if pos == len(valores) - 1:
#         print(f'Fim')
