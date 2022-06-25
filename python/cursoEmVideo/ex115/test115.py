from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'dados.txt'
if not arqExiste(arq):
    arqCria(arq)
while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if opc == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerDados(arq)
    elif opc == 2:
        cabecalho('NOVO CADASTRO')
        addDados(arq)
    else:
        cabecalho('Saindo do sistema... Ate logo!')
        break
    sleep(1)