import os

os.system("clear")

cpf_cadastrado = "1905050"
senha_cadastrada = "1221"
data_cadastrada = "14022025"
mentor_cadastrada = "carlos"

cpf = input("digite seu cpf: ")
senha = input("digite sua senha: ")
data = input("digite a data de hj: ")
mentor = input("digite seu mentor: ")


if cpf_cadastrado == cpf and senha_cadastrada == senha and data_cadastrada == data and mentor_cadastrada == mentor:
    print("Bem Vindo")
else:
    print("login ou senha invalida")

