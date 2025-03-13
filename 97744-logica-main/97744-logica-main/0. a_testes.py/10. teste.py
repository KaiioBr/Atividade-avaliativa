import os

os.system("clear") # Limpa o Terminal.

nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))
nota_3 = float(input("Digite sua nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 7:
    print(f"reprovado: {media}")
else:
    print("Aprovado!!!")    

print()
print(f"Media:{media}")