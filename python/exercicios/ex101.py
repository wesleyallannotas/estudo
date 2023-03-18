def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-'*20)
nascimento = int(input('Em que ano voce nasceu? '))
print(voto(nascimento))