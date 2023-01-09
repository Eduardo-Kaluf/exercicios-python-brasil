from unittest import result


x = float(input("insira o primeiro número: "))
y = float(input("insira o segundo número: "))
z = float(input("insira o terceiro número: "))

if x > y and x > z:
  bigger = x
elif y > x and y > z:
  bigger = y
else:
  bigger = z

if x < y and x < z:
  lower = x
elif y < x and y < z:
  lower = y
else:
  lower = z

if x > y and x < z or x > z and x < y:
  medium = x
elif y > x and y < z or y < x and y > z:
  medium = y
else:
  medium = z

Resultado = f"Seus números em ordem decrescente são: {bigger}, {medium} e {lower}"

print(Resultado)
