import os

os.system("clear")

import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 100)
tentativa = 0

print("Tente adivinhar o número entre 1 e 10!")

while True:
    tentativa += 1
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_secreto:
        print("Tente um número maior!")
    elif palpite > numero_secreto:
        print("Tente um número menor!")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break