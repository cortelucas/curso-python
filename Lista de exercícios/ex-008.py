# Escreva um programa que leia um valor em metros e o exiba convertido em quilometros, hectometros, decametro, decimentros, centimetro e milimetros.

m = float(input('Digite uma distância em metros: '))

print(f'A medida de {m}m correspode a: \n-{m/1000} km \n-{m/100} hm \n-{m/10} dam \n-{m*10} dm \n-{m*100} cm \n-{m*1000} mm')
