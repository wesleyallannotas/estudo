from time import sleep

def contagem(x, y, z):
    print('-=' * 15)
    print(f'Contagem de {x} ate {y} de {z} em {z}')
    # USANDO FOR
    if z < 0:
        z = abs(z)
    elif z == 0:
        z = 1
    if x > y:
        z = -z
        y -= 1
    else:
        y += 1
    for i in range(x, y, z):
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
    print('FIM')

    # # USANDO WHILE
    # if z < 0:
    #     z = abs(z)
    # if z == 0:
    #     z = 1
    # if x < y:
    #     cont = x
    #     while cont <= y:
    #         print(f'{cont} ', end='', flush=True)  # fluse=False evita buffer de tela.
    #         cont += z
    #         sleep(0.3)
    #     print('FIM')
    # else:
    #     cont = x
    #     while cont >= y:
    #         print(f'{cont} ', end='', flush=True)
    #         cont -= z
    #         sleep(0.3)
    #     print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 15)
print('Agora e sua vez de personalizar a contagem!')
x = int(input('Inicio: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contagem(x, y, z)
