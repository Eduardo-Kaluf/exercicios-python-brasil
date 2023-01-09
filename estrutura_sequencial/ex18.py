Tamanho = float(input("Insira o tamanho do arquivo em MB: "))

Velocidade = float(input("Qual a velocidade de sua Internet em Mbps? "))

Tempo = (Tamanho / (((Velocidade * 60) / 8 )))


Resultado = f"O tempo médio para o download de seu arquivo é {Tempo}"

print(Resultado)
