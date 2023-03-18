fraseBase = str(input('Digite uma frase: ')).strip().upper()
fraseLista = fraseBase.split()
frase = ''.join(fraseLista)
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print(f'A frase digitada foi {frase} a inversa e {inverso}')
if frase == inverso:
    print('E um palindromo')
else:
    print('Nao e um palindromo')

# Exclusivo Python
'''
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
print(f'O inverso de {frase} e {frase[::-1]}')
if frase == frase[::-1]:
    print('E um palindromo')
else:
    print('Nao e um palindromo')
'''
