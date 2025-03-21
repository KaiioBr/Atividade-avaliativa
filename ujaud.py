import os
import time
os.system("clear")

print("""
======================= MENU =======================
Codigo  \t\tprato   \t\tvalor                         
1  \tPicanha    \t25,00                               
2  \t\tLasanha  \t25,00                               
3  \t\tStrogonoff   \t\t18,00                         
4  \t\tBife acebolado   \t\t15,00                     
5  \t\tPao com ovo  \t\tDe graça bebe                 
====================================================  
""")

opcao = int(input("digite a opçao desejada: "))

match opcao:
    case 1:
        prato = "Picanha"
        valor = 25
    case 2:
        prato = "Lasanha"
        valor = 25
    case 3:
        prato = "strogonoff"
        valor = 18
    case 4:
        prato = "Bife acebolado"
        valor = 15
    case 5:
        prato = "Pao com ovo"
        valor = 00
    case _:
        resultado = "Opçao invalida" 

desejo = str(input("Deseja comprar mais algum ? "))

match desejo:
    case "sim":
            opcao2 = int(input("Digite a opçao desejada2: "))
           
            match opcao2:
                case 1:
                    prato2 = "Picanha"
                    valor2 = 25
                case 2:
                    prato2 = "Lasanha"
                    valor2 = 25
                case 3:
                    prato2 = "strogonoff"
                    valor2 = 18
                case 4:
                    prato2 = "Bife acebolado"
                    valor2 = 15
                case 5:
                    prato2 = "Pao com ovo"
                    valor2 = 00
                case _:
                    resultado = "Opçao invalida" 
        





print()
print(f"Prato(s): {prato}")
print(f"valor: R$ {valor:.2f}")


