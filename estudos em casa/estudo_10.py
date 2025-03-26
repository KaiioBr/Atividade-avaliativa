import os

os.system("clear")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

simbolo = input("Digite um dos simbolos '+' ou '-' ou '*' ou '/' ou 'm' ")

match simbolo:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2 
    case '/':
        resultado = num1 / num2
    case 'm':
        resultado = num1 + num2 / 2
        print()
        if resultado >= 7:
            print("media aprovado: ")
        elif resultado >= 5:
            print("recuperaçao: ")
        else:
            print("Reprovado: ")

print(f"Resultado: {resultado:.1f}")

