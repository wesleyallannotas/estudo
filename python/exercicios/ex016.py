from math import trunc
val = float(input('Digite um valor: '))

# f'string
print(f'O valor digitado foi {val} e a sua porcão inteira e {trunc(val)}')

# Método format
print('O valor digitado foi {} e a sua porcão inteira e {}'.format(val, trunc(val)))

# Usando conversão para inteiro
print(f'O valor digita foi {val} e a sua porcão inteira e {int(val)}')