# Com loop
def somaLoop(lista):
    total = 0
    for x in lista:
        total += x
    return total

# Com recursão
def soma(lista):
    if lista == []:
        return 0
    else:
        # # Utilizando pop
        # return lista.pop() + soma(lista)    
        # Utilizanod Fatiamento
        return lista[0] + soma(lista[1:])   

print(somaLoop([1, 2, 3, 4]))
print(soma([1, 2, 3, 4]))
