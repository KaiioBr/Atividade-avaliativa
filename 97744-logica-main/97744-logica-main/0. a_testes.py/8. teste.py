import os

os.system("clear") # Limpa o Terminal.

print('\t====tabuada====')
numero = float(input("Digite um numero: "))
print('\n Tabuada de', numero, ':')
for i in range(-9, 11):
    print(numero, 'X', i, '=', (numero * i))