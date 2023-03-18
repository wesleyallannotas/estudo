def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: Uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma
    """
    resp = dict()
    resp['total'] = sum(notas)
    resp['maior'] = max(notas)
    resp['menor'] = min(notas)
    resp['media'] = resp['total'] / len(notas)
    if sit:
        if resp['media'] >= 7:
            resp['situação'] = 'BOA'
        elif resp['media'] < 5:
            resp['situação'] = 'RUIM'
        else:
            resp['situação'] = 'RAZOÁVEL'
    return resp


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)