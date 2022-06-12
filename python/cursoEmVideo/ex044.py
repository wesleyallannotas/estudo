print('\033[1;33m-=\033[m'*12 + ' \033[1;36mLOJAS WSILVA \033[m' + '\033[1;33m=-\033[m'*12)
#print('{:=^40}'.format(' LOJAS WSILVA '))
compra = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual e a opcao? '))
if opcao == 1:
    print(f'Sua compra sera a vista no dinheiro/cheque de R${compra:.2f} \033[1;32mCOM DESCONTO\033[m')
    print(f'Sua compra de R${compra:.2f} vai custar R${compra * 0.9:.2f} no final')
elif opcao == 2:
    print(f'Sua compra sera a vista no cartao de R${compra:.2f} \033[1;32mCOM DESCONTO\033[m')
    print(f'Sua compra de R${compra:.2f} vai custar R${compra * 0.95:.2f} no final')
elif opcao == 3:
    print(f'Sua compra sera em 2x no cartao de R${compra / 2:.2f} \033[1;33mCOM PRECO FORMAL\033[m de R${compra:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra de R${compra:.2f} sera em {parcelas}x no cartao de R${compra / parcelas:.2f} \033[1;31mCOM JUROS\033[m')
    print(f'Sua compra de R${compra:.2f} vai custar R${compra * 1.20:.2f} no final')
else:
    print('Opcao \033[1;31mINVALIDA\033[m Tente novamente!')
