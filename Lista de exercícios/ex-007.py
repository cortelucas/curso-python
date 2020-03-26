# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nt1 = float(input('Digite a primeira nota do aluno: '))
nt2 = float(input('Digite a segunda nota do aluno: '))
m = (nt1+nt2)/2

print(f'A média entre {nt1} e {nt2} é igual a {m:.1f}')