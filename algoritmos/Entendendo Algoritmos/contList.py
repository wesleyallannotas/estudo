# Função Recursiva
def contList(lst):
    if lst == []:
        return 0
    else:
        return 1 + contList(lst[1:])
        # # Utilizando pop
        # lst.pop()
        # return 1 + contLista(lst)


print(contList([1, 2, 3, 4, 5, 6]))
