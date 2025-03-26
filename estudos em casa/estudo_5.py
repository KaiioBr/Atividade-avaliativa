import os

os.system("clear")

soma = 0
contador = 0

while True:
    nota = int(input("Digite sua nota: "))
    soma += nota
    contador += 1

    desejar = input("quer add mais uma nota senhor ? ")
    if desejar == "n":
        break

media = soma / contador

print()
print(f"Sua media e de {media:.1f}")