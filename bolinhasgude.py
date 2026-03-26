import math
quantidadebolinha = int(input("Quantas bolinhas você irá botar na caixa?"))
tamanhobolinha = int(input("Digite de acordo com o tamanho da bolinha. Pequena = 1 / Média = 2 / Grande = 3"))
match tamanhobolinha:
     case 1:
        quantidadecaixa = quantidadebolinha/550
        print(f"A quantidade de caixas necessárias para embalar as bolinhas será: {math.ceil(quantidadecaixa)}")
     case 2:
        quantidadecaixa = quantidadebolinha/300
        print(f"A quantidade de caixas necessárias para embalar as bolinhas será: {math.ceil(quantidadecaixa)}")
     case 3:
        quantidadecaixa = quantidadebolinha/150
        print(f"A quantidade de caixas necessárias para embalar as bolinhas será: {math.ceil(quantidadecaixa)}")
     case _:
        print("Número inválido")
