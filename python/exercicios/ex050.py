count = 0
soma = 0
for c in range(0, 6):
    val = int(input('Digite um valor: '))
    if val % 2 == 0:
        count += 1
        soma += val
print(f'Voce digitou {count} numeros pares, a soma dos mesmos resulta em {soma}')
