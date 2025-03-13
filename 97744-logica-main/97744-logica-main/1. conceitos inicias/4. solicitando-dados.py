import os

#limpar terminal.
os.system("clear")

#solicitar dados para o usuario
nome = input("Digite Seu nome PORRAAA: ")
idade = int(input("Digite Sua idade PORRAAA: "))
altura = float(input("Digite Sua altura PORRAAA: "))
fale = input("Sua amiga do seu lado, ela e anao sim ou nao? ")

#  Exibindo dados.
print()
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}")
print(f"sim ou não? {fale}")