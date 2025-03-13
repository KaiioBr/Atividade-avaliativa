import os

os.system("clear") # Limpa o Terminal.

print("""
======================{Preço}======================
A = Alcool       3.79R$
G = Gasolina     6.59R$
P = premium       15R$ 
""")

gaso = input("Digite o tipo do combustivel: ").upper()
litros = int(input("Digite a quantidade de litros: "))

if gaso == "A": 
    preco = 3.79
    Tipo = "Alcool"
elif gaso == "G":
    preco = 6.59
    Tipo = "Gasolina"
elif gaso == "P":
    preco = 15
    Tipo = "premium"

match gaso:
    case "A":
        if litros <= 25:
            desconto = preco * 0.02
        else:
            desconto = preco * 0.04
    case "G":
        if litros <= 25:
            desconto = preco * 0.03
        else:
            desconto = preco * 0.05
    case "P":
        if litros <= 25:
            desconto = preco * 0.04
        else:
            desconto = preco * 0.06
    case _:
        print("Combustivel nao encontrado")
        exit()



valor = preco * litros
valorfinal = valor - desconto
print(f"O valor total a ser pago e de {valorfinal:.2f}R$ no(a) {Tipo}: ")
print(f"voce abasteceu {litros}L")