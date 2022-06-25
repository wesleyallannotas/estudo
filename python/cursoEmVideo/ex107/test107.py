import moeda

preco = float(input('Digite o preço R$'))
print(f'A metade de R${preco} e R${moeda.metade(preco)}')
print(f'O dobro de R${preco} e R${moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R${moeda.aumento(preco, 10)}')
