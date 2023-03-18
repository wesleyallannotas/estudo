from time import sleep

def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    maior = 0
    for i, x in enumerate(num):
        print(f'{x} ', end='', flush=True)
        if i == 0:
            maior = x
        elif x > maior:
            maior = x
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
