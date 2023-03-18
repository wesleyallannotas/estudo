maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c} pessoa: Kg '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')
