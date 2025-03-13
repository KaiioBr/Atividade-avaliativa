import os

os.system("clear") # Limpa o Terminal.

nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))

soma = nota_1 + nota_2
produto = nota_1 * nota_2
menos = nota_1 - nota_2
Divisao = nota_1 / nota_2
media = (nota_1 + nota_2) / 2

maior_numero = max (nota_1, nota_2)
menor_numero = min (nota_1, nota_2)

import os

os.system("clear") # Limpa o Terminal.

print()
print(f"soma: {soma}")
print(f"Subtraçao: {menos}")
print(f"Produto: {produto}")
print(f"Divisao: {Divisao}")
print(f"Media: {media}")
print(f"Maior Numero: {maior_numero}")
print(f"Menor Numero: {menor_numero}")