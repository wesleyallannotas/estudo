num = int(input('Digite um numero inteiro: '))

# f'String
print(f'O Dobro de {num} vale {num*2}\nO Triplo de {num} vale {num*3}\nA raiz quadrada de {num} e igual a {pow(num, 1/2):.2f}.')

# Método Format
print('O dobro de {} vale {}'.format(num, (num*2)))
print('O triplo de {} vale {}'.format(num, (num*3)))
print('A raiz quadrada de {} e igual a {:.2f}'.format(num, (num ** (1/2))))
