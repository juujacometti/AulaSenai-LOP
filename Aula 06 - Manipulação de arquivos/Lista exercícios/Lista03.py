'''Dado um arquivo .csv que contém dados referentes aos pedidos de compras de um e-commerce (arquivo gerado no desafio 2), sua tarefa é ler esse arquivo e converter seu conteúdo em um novo arquivo no formato .json. 
Utilize a biblioteca pandas para realizar essa operação.'''

import pandas as pd

df.read_cvsl("pedidos_ecommerce.csv", index=False)
df.to_json("pedidos_ecommerce.json", index=False)
