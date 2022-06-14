lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')

# Logica Completa
print(f'{"COMPLETA":=^25}')
for cont in range(0, len(lanches)):
    print(lanches[cont])
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posicao {cont}')

# Logica Simplificada
print(f'{"SIMPLIFICADA":=^25}')
for lanche in lanches:
    print(lanche)
for pos, lanche in enumerate(lanches):
    print(f'Eu vou comer {lanche} na posicao {pos}')
