from math import radians, sin, cos, tan

ang = float(input('\033[1;33mDigite o angulo que voce deseja: '))
print(f'\033[mO angulo de {ang} tem o SENO de \033[1;32m{sin(radians(ang)):.2f}\033[m')
print(f'O angulo de {ang} tem o COSSENO de \033[1;32m{cos(radians(ang)):.2f}\033[m')
print(f'O angulo de {ang} tem a TANGENTE de \033[1;32m{tan(radians(ang)):.2f}\033[m')
