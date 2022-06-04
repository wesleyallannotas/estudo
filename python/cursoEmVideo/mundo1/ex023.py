# Primeira Forma
num = int(input('Inform um numero: '))
numero = str(num)
print(f'Analisado o numero {numero}')
print(f'Unidade: {numero[len(numero) - 1]}')
print(f'Dezena: {numero[len(numero) - 2]}')
print(f'Centena: {numero[len(numero) - 3]}')
print(f'Milhar: {numero[:len(numero) - 3]}')

# Segunda Forma (Mais Eficiente)
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centeza: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
