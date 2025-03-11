#Peça dois números para o usuário e imprima qual é o maior.

numero1 = int(input("Dgite um número:\n"))
numero2 = int(input("Dgite um segundo número:\n"))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}.")

else:
    print(f"O número {numero2} é maior que o número {numero1}")