# # Primeira Solucao
#
# valores = [[], [], [],]
# for p, c in enumerate(valores):
#     for i in range(0, 3):
#         c.append(int(input(f'Digite um valor para [{p}, {i}]: ')))
# for c in valores:
#     for i in range(0, 3):
#         print(f'[{c[i]:^5}]', end=' ')
#     print()

# Segunda Solucao

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-='*35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
