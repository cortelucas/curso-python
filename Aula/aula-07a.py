n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end=' ')
print(f'A Divisão inteira {di} e potência {e}')