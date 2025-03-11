#Peça um número para o usuário e imprima se ele é par ou ípar. E se é múltiplo de 2 ou de 5.

numero = int(input("Digite um número para verificar se ele é par ou ímpar e se ele é múltiplo de 3 ou de 5:\n"))

if numero % 2 == 0:
    print("O número é par")

else:
    print("O número é ímpar")

if numero % 3 == 0:
    print(f"O numero {numero} é múltiplo de 3")

elif numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5")

else:
    print(f"O número {numero} não é múltiplo nem de 3 e nem de 5")