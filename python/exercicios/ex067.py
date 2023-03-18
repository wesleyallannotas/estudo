blue = '\033[1;36m'
clear = '\033[m'
while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    for n in range(1, 11):
        print(blue, f'{tab} X {n} = {tab * n}', clear)
