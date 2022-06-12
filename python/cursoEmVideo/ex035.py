print('\033[33m-='*20)
print('\033[36mAnalisador de Triângulos')
print('\033[33m-='*20)
seg1 = float(input('\33[mPrimeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\033[mOs segmentos acima \033[32mPODEM FORMAR\033[m um triangulo')
else:
    print('\033[mOs segmentos acima \033[31mNAO PODEM FORMAR\033[m um triangulo')
