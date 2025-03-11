 #Peça um número para o usuário e imprima a classificação de idade => bebe < 2, criança < 13, adolescente < 18, adulto < 60 e idoso >= 60.

idade = int(input("Digite a sua idade para verificar a classificação:\n"))

if idade < 2:
    print("Classificação: bebê")

elif idade < 13:
    print("Classificação: criança")

elif idade < 18:
    print("Classificação: adolescente")

elif idade < 60:
    print("Classificação: adulto")

else:
    print("Classificação: idoso")



