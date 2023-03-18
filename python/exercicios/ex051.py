# Matematicao
print('\033[1;33m-=\033[m'*12)
print('\033[1;32m10 TERMOS DE UMA PA\033[m')
print('\033[1;33m-=\033[m'*12)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end='\033[1;36m ➙ \033[m')
print('ACABOU')

# Logica
'''
print('\033[1;33m-=\033[m'*12)
print('\033[1;32m10 TERMOS DE UMA PA\033[m')
print('\033[1;33m-=\033[m'*12)
iniTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = iniTermo
for c in range(0, 10):
    print(termo, end='\033[1;36m ➙ \033[m') 
    termo += razao
print('ACABOU')
'''
