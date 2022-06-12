cont = numSoma = num = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    numSoma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou {cont} e a soma entre eles foi {numSoma}.')
