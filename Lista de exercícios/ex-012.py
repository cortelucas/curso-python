#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoProduto = float(input('Qual é o preço do produto? R$'))
desconto = precoProduto*0.05

print(f'O produto que custava R${precoProduto}, na promoção com desconto de 5% vai custar R${precoProduto-desconto:.2f}')