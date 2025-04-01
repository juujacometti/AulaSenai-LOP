# Escreva um programa que peça ao usuário 5 números e exiba o maior deles usando o loop while

# Modo 1:
numero1 = float(input("Digite o 1° número:\n"))
numero2 = float(input("Digite o 2° número:\n"))
numero3 = float(input("Digite o 3° número:\n"))
numero4 = float(input("Digite o 4° número:\n"))
numero5 = float(input("Digite o 5° número:\n"))

maior1 = 0
numeros = 0

while numeros < 5:
    if maior1 < numero1:
        maior1 = numero1

    if maior1 < numero2:
        maior1 = numero2

    if maior1 < numero3:
        maior1 = numero3

    if maior1 < numero4:
        maior1 = numero4

    if maior1 < numero5:
        maior1 = numero5

    numeros = numeros + 1

print(f"O maior número entre esses 5 é = {maior1}")


# Modo 2:

contador = 1
maior = float(0.0)

while contador < 5:
    valor = float(input("\nDigite um número:\n"))

    if valor > maior:
        maior = valor
        contador +=1
print(f"O maior número é: {maior}")
