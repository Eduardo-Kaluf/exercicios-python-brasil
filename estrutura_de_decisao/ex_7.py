x = float(input("insira o primeiro número: "))
y = float(input("insira o segundo número: "))
z = float(input("insira o terceiro número: "))

if x > y and x > z:
  high = x
elif y > x and y > z:
  high = y
else:
  high = z

if x < y and x < z:
  low = x
elif y < x and y < z:
  low = y
else:
  low = z

print(low, high)


# if x > y and x > z and y > z:
#   print(x, z)
# elif z > y:
#   print(x, y)

# if y > x and y > z and x > z:
#   print(y, z)
# elif z > x:
#   print(y, x)

# if z > x and z > y and x > y:
#   print(z, y)
# elif y > x:
#   print(z, x)
