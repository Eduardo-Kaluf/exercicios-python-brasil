from math import ceil


Área = float(input("Qual é a área a ser pintada em m²: "))

Tinta_Área = (18 * 3)

Balde = (Área / Tinta_Área)

Balde_arredondado = round(Balde + 0.5)

Preço = (Balde_arredondado * 80)


Resultado = f"Você irá precisar de {Balde_arredondado} e o valor total da compra será de {Preço}"

print(Resultado)  
