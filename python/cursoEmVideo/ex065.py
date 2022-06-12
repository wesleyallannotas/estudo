continuar = 'S'
num = soma = cont = maior = menor = 0
while continuar =='S':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
    continuar = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Invalido! Tente novamento,Quer Continuar? [S/N]')).strip().upper()[0]
print(f'Voce digitou {cont} numeros e a media foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
