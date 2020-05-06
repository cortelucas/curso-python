# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
catOposto = float(input('Insira o cateto oposto: '))
catAdjacente = float(input('Insira o cateto adjacente: '))

print(f'A hipotenusa é {hypot(catOposto, catAdjacente):.2f}!')
