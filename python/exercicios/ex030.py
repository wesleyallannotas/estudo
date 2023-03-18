num = int(input('Me diga um numero qualquer: '))
print(f'O numero {num} e \033[1;33mPar' if (num%2) == 0 else f'O numero {num} \033[1;35mImpar')