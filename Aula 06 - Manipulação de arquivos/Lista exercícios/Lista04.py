'''
Dada uma mensagem criptografada com a cifra de César e um deslocamento conhecido (3), seu objetivo é escrever um programa em Python para descriptografar a mensagem e recuperar o texto original contido no arquivo “criptografado.txt”.
Observações:
- O arquivo deve ser lido com `encoding="utf-8"`.
- A cifra afeta apenas letras do alfabeto. Espaços, números e pontuações devem permanecer inalterados.
'''
import os

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("criptografado.txt", "r", encoding="utf-8") as file: # Abre o arquivo com as criptografias
    conteudo_criptografado = file.read().lower() # Padronização de todas as letras para minusculas

deslocamento = 3 # Define a quantidade do deslocamento
conteudo_descriptografado = ""

for letra in conteudo_criptografado:
    if letra in alfabeto:
        posicao_atual = alfabeto.index(letra)
        nova_posicao = (posicao_atual - deslocamento) % len(alfabeto) # Calcula a nova posição das letras aplicando o deslocamento inverso
        conteudo_descriptografado += alfabeto[nova_posicao]
    else:
        conteudo_descriptografado += letra

print(conteudo_descriptografado)

with open("Texto_Descriptografado.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_descriptografado)