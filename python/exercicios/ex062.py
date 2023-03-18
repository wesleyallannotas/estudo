# While and if
'''
print('Gerador de PA')
print('-='*10)
iniTermo = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = iniTermo
cont = 1
delimitador = 10
while cont <= delimitador:
    print(termo, end=" - ")
    if cont == delimitador:
        print('PAUSA')
        delimitador += int(input('Quantos termos voce quer mostrar a mais? ')) 
    termo += razao
    cont += 1
print('FIM')
'''

# While and While
print('Gerador de PA')
print('-='*10)
iniTermo = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = iniTermo
cont = 1
delimitador = 0
mais = 10
while mais != 0:
    delimitador += mais
    while cont <= delimitador:
        print(termo, end=" - ")
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termo voce quer mostrar a mais? '))
print(f'Progessao finalizadad com {delimitador} termos mostrados')
