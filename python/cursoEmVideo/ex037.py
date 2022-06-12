num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao: 
[ 1 ] Converter para \033[1;32mBINARIO\033[m
[ 2 ] Converter para \033[1;33mOCTAL\033[m
[ 3 ] Converter para \033[1;36mHEXADECIMAL\033[m''')
opcao = int(input('Sua opçao: '))

# Primeira Forma
# if opcao == 1:
#     convertido = bin(num)
#     base = '\033[1;32mBINARIO\033[m'
# elif opcao == 2:
#     convertido = oct(num)
#     base = '\033[1;33mOCTAL\033[m'
# elif opcao == 3:
#     convertido = hex(num)
#     base = '\033[1;36mHEXADECIMAL\033[m'
# else:
#     convertido = '000'
#     base = '\033[1;31minvalido\033[m'
# print(f'{num} convertido para {base} e igual a \033[1;31m{convertido[2::]}\033[m')

# Segunda Forma
if opcao == 1:
    print(f'{num} convertido para \033[1;32mBINARIO\033[m e igual a \033[1;31m{bin(num)[2:]}\033[m')
elif opcao == 2:
    print(f'{num} convertido para \033[1;33mOCTAL\033[m e igual a \033[1;31m{oct(num)[2:]}\033[m')
elif opcao == 3:
    print(f'{num} convertido para \033[1;36mHEXADECIMAL\033[m e igual a \033[1;31m{hex(num)[2:]}\033[m')
else:
    print('\033[1;31mOpcao invalida, tente novamente.\033[m')
