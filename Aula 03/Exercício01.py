#Faça um programa que solicita a idade de m usuário e mostra em tela se ele for maior de idade ou menor de idade

idade = int(input("Digite a sua idade para verificar se é maior ou menor de idade:\n"))

if idade < 18:
    print("Você ainda é menor de idade!")

else:
    print("Você já é maior de idade!")