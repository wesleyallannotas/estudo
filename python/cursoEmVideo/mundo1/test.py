n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro:'))
s = n1 + n2

while s < 10:
    print('Valor baixo tente novamente')
    n1 = int(input('Digite um valor: ')) 
    n2 = int(input('Digite outro: '))
    s = n1 + n2


print('A Soma de {} e {} vale {}'.format(n1, n2, s))