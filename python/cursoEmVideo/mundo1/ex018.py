from math import radians, sin, cos, tan

ang = float(input('Digite o angulo que voce deseja: '))
print(f'O angulo de {ang} tem o SENO de {sin(radians(ang)):.2f}')
print(f'O angulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f}')
print(f'O angulo de {ang} tem a TANGENTE de {tan(radians(ang)):.2f}')
