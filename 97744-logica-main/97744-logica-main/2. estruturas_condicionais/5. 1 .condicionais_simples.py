import os

os.system("clear") # Limpa o Terminal.

# solicitando dados
idade = int(input("Digite sua idade: "))


# verificando dados
if idade < 18:
    print("Cai fora pirralho!")
if idade > 18:
    print("e noix")    


# exibindo dados (saida)
print()
print(f"Idade: {idade}")


print("== Fim ==")