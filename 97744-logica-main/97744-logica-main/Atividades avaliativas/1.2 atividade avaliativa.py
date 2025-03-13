import os

os.system("clear") # Limpa o Terminal.

nome = str(input("Digite Seu nome: "))
sexo = str(input("Digite Seu Sexo: ")).lower()

match sexo:
    case "f":
        estado_civil = str(input("Digite Seu estado civil: ")).lower()
        if estado_civil == "casada":
            ano = int(input("Digite o ano de casados: "))
            print(f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome}Estado civil Solteira(o)")
    case "m":
        estado_civil = str(input("Digite Seu estado civil: ")).lower()
        if estado_civil == "casado":
            ano = int(input("Digite o ano de casados: "))
            print(f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome}Estado civil Solteira(o)")
    case _:
        print("Algo esta errado:")