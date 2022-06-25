cor = {'yellow':'\033[33m', 'blue':'\033[36m', 'red':'\033[31m', 'green':'\033;32m', 'clear':'\033[m'}

def linha(qnt=50):
    return '-' * qnt

def cabecalho(msg):
    print(linha())
    print(msg.center(50))
    print(linha())
    
def opcao(lst):
    for i, opc in enumerate(lst):
        print(f'{cor["yellow"]}{i+1} - {cor["blue"]}{opc}{cor["clear"]}')

def escolha(msg):
    while True:
        try:
            opc = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cor["red"]}ERRO! por favor, digite um numero inteiro valido.{cor["clear"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cor["red"]}\nEntrada de dado cancelada! {cor["clear"]}')
            return 3
        else:
            if opc > 0 and opc <= 4:
                return opc
            print(f'{cor["red"]}ERRO! Digite um opção valida!{cor["clear"]}')
            continue

def menu(lst):
    while True:
        cabecalho('MENU PRINCIPAL')
        opcao(lst)
        opc = escolha('Sua Opção: ')
        return opc