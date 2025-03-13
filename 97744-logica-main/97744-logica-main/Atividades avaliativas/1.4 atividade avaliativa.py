import os

os.system("clear") # Limpa o Terminal.

print("""
======================= MENU =======================
         Frutas      preço ate 5 kg     preço acima 5 kg      
 \t\t    maça           2,50                 2,20
 \t\t    murango        1,80                 1,50      
====================================================  
""")

quant_murango = float(input("Diga a quantidade de murango: "))
quant_maca = float(input("Diga a quantidade de maças: "))


maca = float(2.50)
maca_2 = float(2.20)
murango = float(1.80)
murango_2 = float(1.50)


if quant_maca or quant_murango <=5:
    total=(quant_murango*murango)+(quant_maca*maca)
    print(f"Total: {total} ")
elif quant_maca or quant_murango > 8:
    total=(quant_murango*murango)+(quant_maca*maca)
    Total_final=(total*0.10)
    print(f"Valor a ser pago: {Total_final} ")

