x = float(input("insira a sua primeira nota: "))
y = float(input("insira a sua segunda nota: "))

Média = ((x + y) / 2)

if Média >= 7 and Média < 10:
  print("Aprovado!")
elif Média < 7:
  print("Reprovado ): ")
else:
  print("Aprovado com Distinção")

