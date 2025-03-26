import os

os.system("clear")

contador = 0
soma = 0

while True:
    nota = float(input("Digite a sua nota: "))
    soma += nota
    contador += 1

    desejo = input("Deseja add mais uma nota ? ")
    if desejo == "n":
        break

media = soma / contador

print()
print(f"Sua media e {media}")
