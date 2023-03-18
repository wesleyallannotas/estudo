val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor: '))
val3 = int(input('Terceiro valor: '))
# Primeira Forma (Pessoal)
if val1 > val2 and val1 > val3:
    maior = val1
    if val2 < val3:
        menor = val2
    else:
        menor = val3
elif val2 > val1 and val2 > val3:
    maior = val2
    if val1 < val3:
        menor = val1
    else:
        menor = val2
else:
    maior = val3
    if val1 < val2:
        menor = val1
    else:
        menor = val2

# Segunda Forma (Professor)
menor = val1
if val2 < val1 and val2 < val3:
    menor = val2
if val3 < val1 and val3 < val2:
    menor = val3
maior = val1
if val2 > val1 and val2 > val3:
    maior = val2
if val3 > val1 and val3 > val2:
    maior = val3
print(f'O menor valor digitado foi \033[1;31m{menor}\033[m')
print(f'O maior valor digitado foi \033[1;32m{maior}\033[m')