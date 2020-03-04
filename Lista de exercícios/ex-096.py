#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def lin():
    print('-'*30)
    

def area(lrg, comp):
    area = lrg*comp
    print(f'A área de um terreno {lrg} X {comp} é de {area}m².')

lin()
print('CONTROLE DE TERRENOS')
lin()

lrg = float(input('Insira a Largura: '))
comp = float(input('Insira a Comprimento: '))

area(lrg, comp)