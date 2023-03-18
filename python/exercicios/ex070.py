nomeBarato = ' '
cont = contCaro = soma = precoBarato =  0
print('-'*40)
print(f'{"LOJA SUPER BARATAO":^40}')
print('-'*40)
while True:
    cont += 1
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preso: R$'))
    soma += preco
    if cont == 1 or preco < precoBarato:
        nomeBarato = nome
        precoBarato = preco
    if preco > 1000:
        contCaro += 1
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break 
    if continuar == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {contCaro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${precoBarato:.2f}')

# # Limpando Variavel
# resp = ' '
# while resp not in 'SN':
#     resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

# # Quebrando Loop
# while True:
#     resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
#     if resp in 'SN':
#         break
