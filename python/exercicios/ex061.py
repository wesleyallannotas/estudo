# Matematica
'''
print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
decimo = termo + (10 - 1) * razao
while termo <= decimo:
    print(termo, end=' - ')
    termo += razao
print('FIM')
'''

# Logica
print('Gerador de PA')
print('-='*10)
iniTermo = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = iniTermo
cont = 1
while cont <= 10:
    print(termo, end=" - ")
    termo += razao
    cont += 1
print('FIM')
