import os
import time
os.system("clear")

# Exemplo de uso do laço de repetiçao while.
while True:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Nao autorizado. \nSomente maiores de 18. \n")
    else:
        break

print("Acesso permitido")
print("Fim")