# Receba uma variável dia, mês e ano. Junte as variáveis e print no formato "dia/mês/ano

dia = 11
mes = 2
ano = 2025

data = "%02d" %dia + "/" + "%02d" %mes + "/" + "%02d" %ano

print(data)