name = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas e {name.upper()}')
print(f'Seu nome em minusculas e {name.lower()}')
print(f'Seu nome tem ao todo {len(name.strip()) - name.count(" ")} letras')
print(f'Seu primeiro nome e {name.split()[0]} e tem {len(name.split()[0])} letras')