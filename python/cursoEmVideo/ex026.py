frase = str(input('Digite uma frase: ')).strip()
print(f'A letra \033[1;32mA\033[m aparece \033[31m{frase.lower().count("a")}\033[m vezes na frase.')
print(f'A primeira letra \033[1;32mA\033[m apareceu na posição \033[31m{frase.lower().find("a")+1}\033[m')
print(f'A ultima letra \033[1;32mA\033[m apareceu a posição \033[31m{frase.lower().rfind("a")+1}\033[m')
