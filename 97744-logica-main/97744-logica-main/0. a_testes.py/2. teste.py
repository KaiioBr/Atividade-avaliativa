import os

os.system("clear")

cpf_cadastrado = input("Digite seu cpf: ")
senha_cadastrado = input("Digite sua senha: ")

cpf = "123"
senha = "321"

if cpf_cadastrado == cpf and senha_cadastrado == senha:
    print("Seja bem vindo")
else:
    print("Rala daqui porra")