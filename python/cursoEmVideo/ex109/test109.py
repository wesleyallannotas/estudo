import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} e {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} e {moeda.dobro(preco, True)}')
print(f'Aumentando 10% de {moeda.moeda(preco)} e {moeda.aumento(preco, 10, True)}')