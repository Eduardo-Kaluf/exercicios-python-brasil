x = float(input("Insira o primeiro lado do triângulo: "))
y = float(input("Insira o segundo lado do triângulo: "))
z = float(input("Insira o terceiro lado do triângulo: "))

if (x + y) > z and (x + z) > y and (y + z) > x:
  Resultado = ("É um triângulo")
else:
  Resultado = ("Não é um triângulo")

print(Resultado)

if Resultado == ("Não é um triângulo"):
  Resultado = ""
  print(Resultado)
elif x == y == z:
  print("Equilatero")
elif (x == y) and x != z or (x == z) and x != y or (z == y) and z != x:
  print("Isósceles")
else:
  print("Escaleno")