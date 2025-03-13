import os
import time
os.system("clear")

print("Contagem de 2 em 2.")
for i in range(100,121):
    if i % 2 == 0:
        print(f"Numero: {i}")
        time.sleep(0.05)