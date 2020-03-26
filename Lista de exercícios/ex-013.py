# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salAnt = float(input('Qual é o salário do funcionário? R$'))
reajuste = salAnt*0.15

print(f'O funcionário que ganhava R${salAnt:.2f} com 15% de aumento, passa a receber R${salAnt+reajuste:.2f}')