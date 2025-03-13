import os

os.system("clear") # Limpa o Terminal.

nmr_1 = float(input("Digite algun numero: "))
nmr_2 = float(input("Digite algun numero: "))
operacao = input("Digite o operador: ")

match operacao:
    case "+":
        resultado = nmr_1 + nmr_2
    case "-":
        resultado = nmr_1 - nmr_2    
    case "*":
        resultado = nmr_1 * nmr_2    
    case "/":
        resultado = nmr_1 / nmr_2
    case _:
        resultado = (f"opçao invalida")    

print()    
print(f"Primeiro numero: {nmr_1}")
print(f"Operaçao: {operacao}")
print(f"Segundo numero: {nmr_2}")
print(f"resultado: {resultado}")