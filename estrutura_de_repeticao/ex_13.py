x = float(input("Base: "))
y = float(input("Expoente: "))
z = 1
i = x

while z < y:
  r = i * x
  i = r
  z = z + 1

print(r)
