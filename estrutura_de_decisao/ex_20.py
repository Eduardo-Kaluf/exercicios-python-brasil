x = float(input("Insira sua primeira nota: "))
y = float(input("Insira sua segunda nota: "))
z = float(input("Insira sua terceira nota: "))

média = ((x + y + z) / 3)

if média == 10:
  print("Aprovado com distinção")
  print(média)
elif média < 10 and média >= 7:
  print("Aprovado")
  print(média)
else:
  print("Reprovado")
  print(média)
