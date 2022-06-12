peso = float(input('Qual e seu peso? (Kg) '))
altura = float(input('Qual e sua altura? (m) '))
imc = peso / altura ** 2
print(f'O IMC dessa pessoa e de {imc:.1f}')
print('Vode esta na faixa de', end=' ')
if imc <= 18.5:
    print('\033[1;31mABAIXO DO PESO\033[m')
elif imc < 25: # 18.5 <= imc < 25 (imc >= 18,5 and imc < 25) 
    print('\033[1;32mPESO IDEAL\033[m')
elif imc < 30:
    print('\033[1;33mSOBREPESO\033[m')
elif imc < 40:
    print('\033[1;31mOBESIDADE\033[m')
else:
    print('\033[1;31mOBESIDADE MORBIDA\033[m')
