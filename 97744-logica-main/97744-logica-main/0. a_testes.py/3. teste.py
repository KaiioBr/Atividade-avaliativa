import os

os.system("clear")

nome_cadastrado = input("Digite seu nome: ")
senha_cadastrado = input("Digite sua senha: ")

nome = "kaio"
senha = "1221"

if nome_cadastrado == nome and senha_cadastrado == senha:
    print("Seja bem vindo")
else:
    print("Rala daqui porra")