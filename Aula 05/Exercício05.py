"""
Calculadora com menu - Faça um programa de calculadora que exibe um menu com as opções: Somar, subtrair, multiplicar, dividir e sair.
O programa deve pedir ao usuário qu eescolha uma opção do menu e, em seguida, dois números para realizar a operação.
o programa continua mostrando o menu até que a opção "sair" seja selecionada.
"""

escolha = 0

print("====================\n*** CALCULADORA ***\n[ + ] Somar\n[ - ] Subtrair\n[ * ] Multiplicar\n[ / ] Dividir\n[ X ] Sair\n====================")

escolha = str(input("Digite o símbolo da operação desejada:\n"))

if escolha == "x" or escolha == "X":
    print("Programa finalizado")

elif escolha == "+" or escolha == "-" or escolha == "*" or escolha == "/":
    while escolha == "+" or escolha == "-" or escolha == "*" or escolha == "/":
        numero1 = float(input("Digite o primeiro valor para realizar a operação:\n"))
        numero2 = float(input("Digite o segundo valor para realizar a operação:\n"))

        if escolha == "+":
            print(numero1 + numero2)

        elif escolha == "-":
            print(numero1 - numero2)

        elif escolha == "*":
            print(numero1 * numero2)

        elif escolha == "/":
            print(numero1 / numero2)
else:
    print("Escolha entre as opções oferecidas.")