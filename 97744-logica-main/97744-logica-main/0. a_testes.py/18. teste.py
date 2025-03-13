import os

os.system("clear") # Limpa o Terminal.

idade = int(input("Digite sua idade: "))

if idade >=18 and idade <=65:
    print("obrigada a votar")
else:
    print("Nao sao obrigados a votar")