#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias foi alugado o carro? '))
km = float(input("Quantos Km's foram rodados? "))
valor_dias = (dias * 60)
valor_km = (km * 0.15)

print(f'O total a pagar é de R${valor_km + valor_dias:.2f}!')
