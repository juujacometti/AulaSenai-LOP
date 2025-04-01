# Faça um programa que exiba a média de uma lista de números (tamanho da lista é definido pelo usuário) usando o loop while

lista = []

quantidade = int(input("Digite a quantidade de números que você deseja que sua lista contenha:\n"))
soma = 0
divisor = quantidade

while quantidade > 0:
    numeros_lista = int(input(f"Digite os números que você deseja inserir na sua lista:\n"))
    lista.append(numeros_lista)
    soma += numeros_lista
    quantidade -= 1

print(f"\nMédia da lista: {soma / divisor}")