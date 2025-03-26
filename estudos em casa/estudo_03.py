import os

os.system("clear")

contado = 0
soma = 0

while True:
    nota = float(input("Digite sua nota: "))
    soma += nota
    contado += 1

    desejo = input("Deseja digitar mais uma nota 'S' ou 'N': ")
    if desejo == "n":
        break

media = soma / contado

print()
print(f"A sua media foi de {media}")