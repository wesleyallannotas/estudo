# Meu algoritmo
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array.pop(len(array)//2)
        sub_min = list()
        sub_max = list()
        for i in array:
            if i > pivo:
                sub_max.append(i)
            else:
                sub_min.append(i)
        return quicksort(sub_min) + [pivo] + quicksort(sub_max)

# Algoritmo Livro 
def quicksortLivro(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksortLivro(menores) + [pivo] + quicksortLivro(maiores)


print(quicksort([]))
print(quicksort([1]))
print(quicksort([2, 1]))
print(quicksort([2, 1, 3]))
print(quicksort([3, 1, 4, 2]))
print(quicksort([5, 2, 3, 1, 4]))
print(quicksort([13, 22, 9, 7, 65, 24, 34, 32]))

print(quicksortLivro([]))
print(quicksortLivro([1]))
print(quicksortLivro([2, 1]))
print(quicksortLivro([2, 1, 3]))
print(quicksortLivro([3, 1, 4, 2]))
print(quicksortLivro([5, 2, 3, 1, 4]))
print(quicksortLivro([13, 22, 9, 7, 65, 24, 34, 32]))
