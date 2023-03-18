val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>>> Qual e sua opcao? '))
    if opcao == 1:
        soma = val1 + val2
        print(f'A soma dos valores e {soma}')
    elif opcao == 2:
        multiplicacao = val1 * val2
        print(f'A multiplicação dos valores e {multiplicacao}')
    elif opcao == 3:
        if val1 > val2:
            print(f'O maior valor e {val1}')
        else:
            print(f'O maior valor e {val2}')
    elif opcao == 4:
        val1 = int(input('Primeiro valor: '))
        val2 = int(input('Segundo valor: '))
    else:
        print('Valor invalido tente novamente')
    print('='*25)
