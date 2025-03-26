import os

os.system("clear")

contador = 0
soma = 0

while True:
    nota = int(input("Digite uma nota: "))
    soma += nota
    contador += 1

    desejo = input("O sr deseja add mais uma nota ? ")
    if desejo == "n":
        break

media = soma / contador

print()
print(f"Sua media foi de {media}")