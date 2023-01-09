MA = float(input("Quantas maças em kg? "))
MO = float(input("Quantos morangos em kg? "))

if MA <= 5:
  preço_MA = 2.50
else:
  preço_MA = 2.20

if MO <= 5:
  preço_MO = 1.80
else:
  preço_MO = 1.50

preço_MA_total = preço_MA * MA
preço_MO_total = preço_MO * MO

valor_total = preço_MA_total + preço_MO_total

if (MA + MO) > 8 or valor_total > 25:
  desconto = 0.10
  valor_total_desconto = (valor_total - (valor_total * desconto))

if (MA + MO) > 8 or valor_total > 25:
  print(valor_total_desconto)
else:
  print(valor_total)


