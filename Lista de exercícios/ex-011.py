# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = h*l

print(f'Sua parede tem a dimensão de {l}m x {h}m e sua área é de {a}m²\n'
      f'Para pintar essa parede, você precisará de {a/2:.2f}l de tinta.')
