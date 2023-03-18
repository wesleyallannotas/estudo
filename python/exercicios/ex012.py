preco = float(input('Qual e o preço do produto? R$'))
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar {preco - (preco*5/100):.2f}')