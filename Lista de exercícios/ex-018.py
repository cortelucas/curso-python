#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = float(input('Digite um angulo de 0 a 360º: '))

print(f'O SENO deste angulo é: {sin(radians(a)):.2f}\n'
      f'O COSSENO deste angulo é: {cos(radians(a)):.2f}\n'
      f'A TANGENTE deste angulo é: {tan(radians(a)):.2f}')
