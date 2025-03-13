import os

os.system("clear") # Limpa o Terminal.

a = int(input("Algoritimo a: "))
b = int(input("Algoritimo b: "))
c = int(input("Algoritimo c: "))

soma = a + b

if a + b < c:
     print("A + B e menor que C: ")
     print(f"valor da soma: {soma}")
else:
    print("A + B e maior que C: ")
    
