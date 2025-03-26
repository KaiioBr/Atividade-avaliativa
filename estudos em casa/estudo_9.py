import os

os.system("clear")

palavra = input("Digite uma palavra: ")  
invertida = ""  

for letra in palavra:  
    invertida = letra + invertida  # Adiciona cada letra no início da nova string  

print("Palavra ao contrário:", invertida)