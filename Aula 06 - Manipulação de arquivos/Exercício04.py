# XML: Crie um arquivo xml chamado "config.xml" e adicione um elemento "config" com subelemento "versão" tendo valor "1.0"
# Abra o arquivo "config.xml" e mostre o valor do subelemento "versão" na tela

xml_str = """<?xml version="1.0" enconding="UTF-8"?>
<config>
    <versao>1.0</versao>
</config>"""

with open("config.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

with open("config.xml", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

