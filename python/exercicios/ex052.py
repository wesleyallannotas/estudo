num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(f'\033[1;33m{c}', end=' ')
    else:
        print(f'\033[1;31m{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisivel {cont} vezes')
if cont > 2:
    print('E por isso \033[1;31mNAO E PRIMO\033[m')
else:
    print('E por isso \033[1;33mE PRIMO\33[m')
