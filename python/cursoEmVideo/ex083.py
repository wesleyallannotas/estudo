# # Utilizando Analise de String
# conAb = 0
# conFec = 0
# exp = str(input('Digite uma expressão: '))
# for c in range(0, len(exp)-1):
#     if c == '(':
#         contAb += 1
#     elif c == ')':
#         contFec += 1
# if conAb == conFec:
#     print('Expressão valida')
# else:
#     print('Expressão invalida')

# Utilizando Lista
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta invalida')