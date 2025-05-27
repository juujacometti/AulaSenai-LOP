#01 TXT. Crie um arquivo txt chamado "meu_arquivo.txt" e escreva "Olá, Mundo" e "Python é divertido!" nele.
#02 Abra o arquivo "meu_arquivo.txt" e leia seu conteúdo, mostrando-o na tela.

with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Python é divertido!\n")

with open("meu_arquivo.txt", "r") as arquivo:
    print(arquivo.read())
