seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

# Forma 1
#if seg1 == seg2 == seg3:
#    print('Os segmentos acima \033[1;31mPODEM FORMAR\033[m um triangulo \033[1;33mEQUILATERO!\033[m')
#elif seg1 == seg2 != seg3 or seg1 != seg2 == seg3 or seg1 == seg3 != seg2:
#    print('Os segmentos acima \033[1;31mPODEM FORMAR\033[m um trianglu \033[1;33mISOSCELES\033[m')
#elif seg1 != seg2 != seg3:
#    print('Os segmentos acima \033[1;31mPODEM FORMAR\033[m um triangulo \033[1;33mESCALENO\033[m')

# Forma 2 (Inteligente)
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima \033[1;31mPODEM FORMAR\033[m um triangulo', end=' ')
    if seg1 == seg2 == seg3:
        print('\033[1;33mEQUILATERO!\033[m')
    elif seg1 != seg2 != seg3 != seg1:
        print('\033[1;33mESCALENO\033[m')
    else:
        print('\033[1;33mISOSCELES\033[m')
else:
    print('\033[mOs segmentos acima \033[1;31mNAO PODEM FORMAR\033[m um triangulo')
