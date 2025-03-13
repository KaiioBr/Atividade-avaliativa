import os

os.system("clear") # Limpa o Terminal.

maca = int(input("Digite seu numero: "))
pera = int(input("Digite seu numero: "))

maior_numero = max (maca, pera)
menor_numero = min (maca, pera)

print()
print(f"Maior Numero: {maior_numero}")
print(f"Menor Numero: {menor_numero}")