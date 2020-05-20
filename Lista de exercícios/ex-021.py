nome = input('Insira o seu nome completo: ')
divi = nome.split()

print(f'O nome com todas letras maiuscualas é {nome.upper()}\n'
      f'O nome com todas letras minúsculas é {nome.lower()}\n'
      #f'O nome tem {len(nome.split)} letras.\n'
      f'O primeiro nome tem {len(divi[0])} letras')