import os

os.system("clear") # Limpa o Terminal.

macas = float(input("Digite seu numero: "))

if macas < 12:
    preco = 1.30
else:
    preco = 1.00

valor = macas * preco

print()
print(f"Valor total: {valor:.2f}")
