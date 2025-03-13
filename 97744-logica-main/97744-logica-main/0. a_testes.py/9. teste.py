import os

os.system("clear") # Limpa o Terminal.

nmr = int(input("Dgiti um numero: "))
if nmr > 10:
    print("e maior que 10!!!")
elif nmr < 10:
    print("nao e maior que 10!!!")
else:
    print("sao iguais!!!")