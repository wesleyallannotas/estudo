from time import sleep
name = input('\033[1;32mDigite seu nome completo: ')
print('\033[1;36mAnalisando seu nome...\033[m')
sleep(1)
print(f'Seu nome em maiúsculas e \033[1;33m{name.upper()}\033[m')
print(f'Seu nome em minusculas e \033[1;34m{name.lower()}\033[m')
print(f'Seu nome tem ao todo \033[1;35m{len(name.strip()) - name.count(" ")} letras\033[m')
print(f'Seu primeiro nome e \033[1;36m{name.split()[0]} e tem {len(name.split()[0])} letras\033[m')