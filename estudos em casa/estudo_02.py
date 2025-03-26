import os

os.system("clear")


    
contador = 0
soma = 0

while True: 
    nota = int(input("Digite uma nota: "))
    soma += nota
    contador += 1

    desejo = input("Deseja adicionar mais uma nota ? ")
    if desejo == "n":
     break

media = soma / contador

print()
print(f"Media: {media}")
print()
if media >= 7:
    print("APROVADO: ")
elif media >= 5 and media < 7: 
    print("Recuperaçao")
else:
    print("Reprovado")
print()