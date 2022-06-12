salario = float(input('Qual e o salario do funcionário? R$'))
# Primeira Forma
aumento = salario * 1.10 if salario > 1250.0 else salario * 1.15

# Segunda Forma
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava \033[1;31mR${salario:.2f}\033[m passa a ganhar \033[1;32mR${aumento:.2f}\033[m agora.')