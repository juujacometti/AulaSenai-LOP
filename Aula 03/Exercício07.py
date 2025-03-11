# Verificação de triângulo. Crie um programa que solicita três comprimentos e determina se esses comprimentos podem formar um triângulo. Se sim, classifique-os como equilátero, escaleno ou isosceles.

lado1 = float(input("Informe três valores para saber se eles formam um triângulo e se formarem, qual a sua classificação.\nDigite o primeiro valor:\n"))
lado2 = float(input("Digite o segundo valor:\n"))
lado3 = float(input("Digite o terceiro valor:\n"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os valores digitados podem formar um triângulo.")

    if lado1 == lado2 and lado1 == lado3:
        print("Os valores digitados formam um triângulo equilátero.")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores digitados formam um triângulo isósceles.")

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Os valores digitados formam um triângulo escaleno.")

else:
    print("Os valores digitados não podem formar um triângulo.")





