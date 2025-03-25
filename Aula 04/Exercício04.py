# Faça um programa que peça ao usuário um número e imprima a tabuada desse número ate 10

numero = int(input("Digite um número inteiro para descobrir a tabuada dele:\n"))
mult = 0

for tabuada in range(1, 11):
    mult *= numero
    print(f"{numero} * {tabuada} = {numero * tabuada}")
