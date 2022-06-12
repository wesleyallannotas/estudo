distancia = float(input('Qual a distancia da sua viagem? '))
print(f'Voce esta prestes a começar uma viagem de {distancia}Km.')

# Primeira Forma 
print(f'E o preço da sua passagem sera de R${distancia * 0.50:.2f}' if distancia <= 200 else f'E o preço da sua passagem sera de R${distancia * 0.45:.2f}')

# Segunda Forma
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua viagem sera de \033[1;32mR${preco:.2f}\033[m')

# Terceira Forma 
if distancia <= 200:
    print(f'E o preço da sua passagem sera de R${distancia * 0.50:.2f}')
else:
    print(f'E o preço da sua passagem sera de R${distancia * 0.45:.2f}')