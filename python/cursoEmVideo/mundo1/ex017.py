from math import hypot, sqrt

catOp = float(input('Comprimento do cateto oposto: '))
catAdj = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(catOp, catAdj):.2f}')
print(f'A hipotenusa vai medir {sqrt((catOp * catOp) + (catAdj * catAdj)):.2f}')
print(f'A hipotenusa vai media {(catOp ** 2 + catAdj ** 2) ** (1/2):.2f}')