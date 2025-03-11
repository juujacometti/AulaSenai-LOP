# Conversor de unidades. Escreva um programa que permite ao usuário escolher entre converter uma temperatura de Celsius para Fahrenheit ou vice-versa. Solicite o valor e execute.

escolha = int(input("Você deseja converter a temperatura para \n1-> Celsius\n2-> Fahrenheit?\n"))
temperatura = float(input("Digite a temperatura que você deseja converter:\n"))

if escolha == 1:
    print(f"A temperatura {temperatura} convertida para graus Celsius é {(temperatura - 32) / 1.8}")

elif escolha == 2:
    print(f"A temperatura {temperatura} convertida para Fahrenheit é {temperatura * 1.8 + 32}")
