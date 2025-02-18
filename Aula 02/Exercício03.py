# Escreva um programa que calcule o valor de uma prestação em atraso, adicionando a taxa de juros de 10% ao valor original da prestação.

prestacao = int(input("Digite o valor da sua prestação em atraso: "))

total = (prestacao * 0.1) + prestacao

print("O valor que deverá ser pago é: ", total)