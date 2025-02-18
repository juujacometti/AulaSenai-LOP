# Crie três variáveis n1, n2 e n3, e calcule a média ponderada desse três valores, considerando os pesos 2, 3 e 5, respectivamente.

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))

media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)

print("A média ponderada dos valores digitados é: ", media_ponderada)