import os

os.system("clear") # Limpa o Terminal.



numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite um numero: "))
operador = input("Digite o operador: ")

match operador:
    case "+":
        resultado = numero_1 + numero_2
    case "-":
        resultado = numero_1 - numero_2 
    case "*":
        resultado = numero_1 * numero_2 
    case "/":    
        resultado = numero_1 / numero_2
    case "0":
        resultado = numero_1 * numero_2 / 3   
    case _:
        resultado = "Opçao invalida"   

print()    
print(f"Primeiro numero: {numero_1}")
print(f"Operaçao: {operador}")
print(f"Segundo numero: {numero_2}")
print(f"resultado: {resultado}")