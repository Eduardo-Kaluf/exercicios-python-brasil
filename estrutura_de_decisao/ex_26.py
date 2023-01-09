combustivel = input("Qual combustivel deseja comprar? (A ou G) ").upper()
litros = float(input("Quantos litros? "))

if combustivel == "A":
  if litros <= 20:
    desconto = 0.03
  else:
    desconto = 0.05

if combustivel == "G":
  if litros <= 20:
    desconto = 0.04
  else:
    desconto = 0.06   



preço_G = ( 2.50 * litros - (2.50 * desconto * litros) )

preço_A = (1.90 * litros - (1.90 * desconto * litros))

if combustivel == "A":
  print(preço_A)
else:
  print(preço_G)