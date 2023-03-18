from datetime import date
nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificacao: \033[1;33mMIRIM\033[m')
elif idade <= 14:
    print('Classificacao: \033[1;33mINFANTIL\033[m')
elif idade <= 19:
    print('Classificacao: \033[1;33mJUNIOR\033[m')
elif idade <= 25:
    print('Classificacao: \033[1;33mSENIOR\033[m')
else:
    print('Classificacao: \033[1;33mMASTER\033[m')
