# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 4.99 #em2017
euro = 5.48
iene = 0.046

print(f'Com R${real} você pode comprar US${real/dolar:.2f}, €{real/euro:.2f} e ¥{real/iene:.2f}.')
