def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: O numero a ser calculado.
    :param show: (opcional) Mostra ou nao a conta.
    :return: O valor do fatorial de um numero num.
    """
    from time import sleep
    f = 1
    for x in range(num, 0, -1):
        if show:
            sleep(0.3)
            print(f'{x} X' if x > 1 else f'{x} =', end=' ', flush=True)
        f *= x
    return f


print('-'*20)
print(fatorial(5, show=True))
print(fatorial(5))