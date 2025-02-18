"""A variável "nome" deve receber o conteúdo "aula" e a variável "nome2" deve receber o conteúdo "Python". Após essa definição, troque o conteúdo das variáveis e imprima"""

nome1 = "aula"
nome2 = "Python"

print(nome1, nome2)

# Criação de uma terceira variável temporária
nome3 = "aula"

nome1 = nome2
print(nome1)

nome2 = nome3
print(nome3)

