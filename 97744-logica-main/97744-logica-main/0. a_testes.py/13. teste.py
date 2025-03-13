import os

os.system("clear")

nu = int(input("Digite um numero: "))

if nu >= 18 and nu <= 65:
     print("Voto obrigatorio")    
elif nu <= 15:
     print ("nao pode votar")
elif nu <= 16 or nu <= 17:
    print("Voto opicional")       
else:
     print("Nao sao obrigado a votar")