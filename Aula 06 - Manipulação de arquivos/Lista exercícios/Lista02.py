"""Dado um arquivo .xls contendo dados referentes aos pedidos de compras de um e-commerce (arquivo gerado no desafio 1), sua tarefa é ler esse arquivo e converter seu conteúdo em um novo arquivo
no formato .csv. Utilize a biblioteca pandas."""

import pandas as pd

df.read_excel("pedidos_ecommerce.xlsx", index=False)
df.to_csv("pedidos_ecommerce.csv", index=False)