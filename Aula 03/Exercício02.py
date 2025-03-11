#Faça um programa que solicite a nota do aluno (float) e imprima se é "Excelente" (>= 9), "Boa" (>= 7 e < 9), Média (>= 5 e < 9), e caso seja abaixo de 5, mostre que é insuficiente.

nota = float(input("Digite a nota do aluno:\n"))

if nota > 10:
    print("A nota digitada está invalida!")

elif nota < 0:
    print("A nota digitada está inválida")

elif nota >= 9:
    print("A sua nota foi Exelente!")

elif nota >= 7:
    print("A sua nota foi boa!")

elif nota >= 5:
    print("A sua nota está na média.")

else:
    print("A sua nota é insuficiente :'(")