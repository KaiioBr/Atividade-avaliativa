import os

os.system("clear")


contador = 0
salario2 = 0
idade2 = 0
maior_idade = 0
menor_idade = 0
sexo2 = str
nome2 = str
while True:
    print("""
\nCodigo | Descriçao
    \n1  |  Adicionar pessoa
    \n2  |  Exibir resultados
    \n3  |  Sair
""")
    codigo = int(input("Add o codigo: "))
    match codigo: 
        case 1:
            sexo = input("Digite 'M' para Masculino e 'F' para Feminino: ")
            nome = input("Nome da pessoa: ")
            idade = int(input("Idade da pessoa: "))
            salario = int(input("Salario da pessoa: "))
            salario2 += salario
            contador += 1
            os.system("clear")
        case 2:
            print()
            print(f"Sexo: {sexo}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Salario: {salario2}")

        case 3:
            break


media_de_salario = salario2 / contador

print()
print(f"Media {media_de_salario}")