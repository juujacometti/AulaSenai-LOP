# Crie um programa que calcule o fatorial de um número dado pelo usuário usando o loop while

numero = int(input("Digite um número:\n"))
fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1

print(f"O fatorial é = {fatorial}")