x = float(input("insira o primeiro número: "))
y = float(input("insira o segundo número: "))
z = float(input("insira o terceiro número: "))

if x > y and x > z:
  print(x)
elif y > z:
  print(y)
else:
  print(z)