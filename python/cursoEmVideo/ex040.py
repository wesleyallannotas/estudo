nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e {media:.1f}')

# Forma 1
#if media < 5.0:
#    print('O aluno esta \033[1;31mREPOROVADO\033[m')
#elif media >= 5.0 and media < 7.0: # Tambem funciona: 7 > media >= 5.0
#    print('O aluno esta de \033[1;33mRECUPERACAO\033[m')
#else:
#    print('O aluno esta de \033[1;32mAPROVADO\033[m')

# Forma 2
if media < 5.0:
    print('O aluno esta \033[1;31mREPOROVADO\033[m')
elif media >= 7.0:
    print('O aluno esta de \033[1;32mAPROVADO\033[m')
else:
    print('O aluno esta de \033[1;33mRECUPERACAO\033[m')
