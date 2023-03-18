distancia = float(input('Uma distancia em metros: '))
# f-string em uma linha
print(f'A mediada de {distancia}m corresponde a\n{distancia/1000}km\n{distancia/100}hm\n{distancia/10}dam\n{distancia*10:.0f}dm\n{distancia*100:.0f}cm\n{distancia*1000:.0f}mm')

# Método format varias linhas
print('A medida de {}m corresponde a'.format(distancia))
print('{}km'.format(distancia/1000))
print('{}hm'.format(distancia/100))
print('{}dam'.format(distancia/10))
# print('{}dm'.format(int(distancia)*10))
print('{:.0f}dm'.format(distancia*10))
# print('{}cm'.format(int(distancia)*100))
print('{:.0f}cm'.format(distancia*100))
# print('{}mm'.format(int(distancia)*1000))
print('{:.0f}mm'.format(distancia*1000))