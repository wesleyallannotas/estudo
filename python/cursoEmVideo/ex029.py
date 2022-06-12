vel = int(input('Qual e a velocidade atual do carro? '))
if vel > 80:
    print('\033[31mMULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    print(f'Voce deve pagar uma multa de \033[1;33mR${(vel - 80) * 7.0:.2f}\033[m')
print('\033[32mTenha um bom dia! Dirija com segurança!')