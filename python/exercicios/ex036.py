valor = float(input('Valor da Casa: R$'))
salario = float(input('Salario do comprador: R$'))
tempo = int(input('Quantos anos quer financiar? '))
prestacao = valor / (tempo * 12) 
print(f'Para pegar uma casa de R${valor:.2f} em {tempo} anos a prestacao sera de \033[1;33mR${prestacao:.2f}\033[m')
if prestacao > salario * 30 / 100:
    print('Emprestimo \033[1;31mNEGADO!')
else:
    print('Emprestimo \033[1;32mAPROVADO!')
