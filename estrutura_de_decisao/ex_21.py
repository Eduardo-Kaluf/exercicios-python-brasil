valor = int(input("Quanto deseja retirar? (min = 10, max = 600) "))

if valor < 10 or valor > 600:
  print("Valor inválido")
  exit()

unidade = valor % 10

dezena = (((valor - unidade) / 10) % 10)

centena = ((((valor - unidade) / 10) - dezena) / 10)

notas_100 = int(centena)

if dezena >= 5:
  notas_50 = 1
else:
  notas_50 = 0 

if dezena < 5:
  notas_10 = int(dezena)
elif dezena > 5:
  notas_10 = int(dezena - 5)
else:
  notas_10 = 0

if unidade >= 5:
  notas_5 = 1
else:
  notas_5 = 0 

if unidade < 5:
  notas_1 = unidade
elif unidade > 5:
  notas_1 = unidade - 5
else:
  notas_1 = 0

Resultado = f"Notas de 100 = {notas_100}, notas de 50 = {notas_50}, notas de 10 = {notas_10}, notas de 5 = {notas_5} e notas de 1 = {notas_1}"

print(Resultado)