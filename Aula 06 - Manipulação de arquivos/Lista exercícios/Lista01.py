"""Dado um conjunto de dados referente aos pedidos de compras de um e-commerce, armazenado em uma lista de dicionários no Python, sua tarefa é gerar um arquivo .xls a partir desses dados. 
Utilize a biblioteca pandas para realizar essa operação."""

import pandas as pd

# Lista para armezenas os pedidos dos usuários
pedidos = []

# Looping para a solicitação dos dados dos pedidos 
while True:
    print("\nDigite os dados do pedido:\n")

    id_pedido = int(input("ID do pedido: "))
    cliente = input("Nome do cliente: ")
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    data = input("Data (dd/mm/aaaa): ")

    pedido = {
        'ID': id_pedido,
        'Cliente': cliente,
        'Produto': produto,
        'Quantidade': quantidade,
        'Preço': preco,
        'Data': data
    }

    pedidos.append(pedido)

    continuar = input("Quer adicionar outro pedido? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Converter para DataFrame e salvar em Excel
df = pd.DataFrame(pedidos) #Transforma listas em tabelas
df.to_excel("pedidos_ecommerce.xlsx", index=False)

print("\nArquivo 'pedidos_ecommerce.xlsx' criado com sucesso!")
print(df)
