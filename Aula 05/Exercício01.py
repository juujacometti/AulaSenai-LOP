# Contagem regressiva. Peça que o usuário digite um número de 5 a 10 e exiba a contagem regressiva.

numero = int(input("Digite um número de 5 a 10:\n"))

if numero >= 5 and numero <= 10:
    while numero > 0:
        numero = numero - 1
        print(numero)

else:
    print("O número escolhido não se encontra nos parâmetros.")