# Crie um programa para um banco que avalia a elegibilidade de empréstimos com base na idade e renda mensal dos clientes. As regras são:
# Clientes com 18 anos ou mais podem pedir um empréstimo se tiverem renda mensal a aprtir de R$1.500,00
# Menores de 18 anos podem obter um empréstimo se tiverem renda mensal acima de R$1.000,00
# Exiba se o cliente é elegível e por qual das duas condições.

idade = int(input("Digite a sua idade:\n"))
renda_mes = float(input("Informe a sua renda mensal:\n"))

if idade >= 18:
    if renda_mes > 1500:
        print("Cliente elegível.\nCliente maior de idade e possui renda maior que R$1.500,00")
    else:
        print("Cliente não elegível para empréstimo.")

elif idade < 18:
    if renda_mes > 1000:
        print("Cliente elegível.\nCliente menor de idade, porém possui renda acima de R$1.000,00")
    else:
        print("Cliente não elegível para empréstimo.")
