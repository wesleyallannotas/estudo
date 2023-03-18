from math import hypot, sqrt

catOp = float(input('\033[1;33mComprimento do cateto oposto: '))
catAdj = float(input('\033[1;36mComprimento do cateto adjacente: '))
print(f'\033[mA hipotenusa vai medir \033[1;32m{hypot(catOp, catAdj):.2f}\033[m')
print(f'A hipotenusa vai medir \033[1;32m{sqrt((catOp * catOp) + (catAdj * catAdj)):.2f}\033[m')
print(f'A hipotenusa vai media \033[1;32m{(catOp ** 2 + catAdj ** 2) ** (1/2):.2f}\033[m')