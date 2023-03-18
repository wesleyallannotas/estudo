largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua area e de {area:.3f}m².')
print(f'Para pintar essa parede, voce precisara de {area/2}l de tinta.')