import os

os.system("clear") # Limpa o Terminal.

login = str(input("Digite seu login: "))
senha = int(input("digite sua senha: "))

login_2 = "kaio"
senha_2 = 1905

if login == login_2 and senha == senha_2:
    print("Bem vindo")
else:
    print("Login ou senha errados")