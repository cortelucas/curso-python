#O  mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
nome = []
i = 0

for i in range(4):
    nome.append(input(f'Insira o {i+1}º nome: '))
random.shuffle(nome)
print(f'A ordem de apresentação será {nome}!')
