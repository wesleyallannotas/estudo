numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito',
           'Dezenove', 'Vinte')
# # While comum
# num = int(input('Digite um numero entre 0 e 20: '))
# while num < 0 or num > 20:
#     num = int(input('\033[1;31mTente novamente.\033[m Digite um numero entre 0 e 20: '))

# While true
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('\033[1;31mTente novamento. \033[m', end='')
print(f'Voce digitou o numero {numeros[num]}')
