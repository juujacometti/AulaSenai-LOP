# Faça um programa que exiba a média de uma lista de números (tamanho da lista é definido pelo usuário)

lista = []

quantidade = int(input("Digite a quantidade de números que você deseja que sua lista contenha:\n"))

for i in range(quantidade):
    numeros_lista = int(input(f"Digite os números que você deseja inserir na sua lista:\n{i + 1} "))
    lista.append(numeros_lista)

print(f"\nSua lista:\n{lista}")