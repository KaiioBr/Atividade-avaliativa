import os

os.system("clear") # Limpa o Terminal.

seu_login = str(input("Digite seu login: "))
sua_senha = int(input("Digite sua senha: "))

login = "Kaio"
senha = 190505

if login == seu_login and senha == sua_senha:
    print("bem vindo")
else:
    print("senha ou login errado")