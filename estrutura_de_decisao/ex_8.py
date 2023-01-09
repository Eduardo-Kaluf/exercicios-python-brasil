x = float(input("insira o primeiro preço: "))
y = float(input("insira o segundo preço: "))
z = float(input("insira o terceiro preço: "))


print("Você deve comprar o produto que custa: ")

if x < y and x < z:
  print(x)
elif y < x and y < z:
  print(y)
else:
  print(z)