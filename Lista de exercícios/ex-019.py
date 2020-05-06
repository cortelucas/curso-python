#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
nome = []
i = 0

for i in range(4):
    nome.append(input(f'Insira o {i+1}º nome: '))
print(f'{random.choice(nome)} apagará o quadro!')
