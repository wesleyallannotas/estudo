import moeda 

preco = float(input('Digite o preço R$'))
print(f'A metade de {moeda.moeda(preco)} e {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} e {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumento(preco, 10))}')
