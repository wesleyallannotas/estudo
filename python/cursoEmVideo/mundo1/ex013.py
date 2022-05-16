salario = float(input('Qual e o salario do funcionario? R$'))
print(f'O funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario+(salario*15/100):.2f}')