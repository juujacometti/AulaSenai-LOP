 # JSON: Crie um arquivo json chamado "dados.json" e insira {"nome": "João", "idade": 25}.
 # Abra o arquivo "dados.json" e mostre seu conteúdo na tela.

import json

with open("dados.json", "w") as f:
    json.dump({"nome": "João", "idade": 25}, f)

with open("dados.json", "r") as f:
    data = json.load(f)
    print(data)