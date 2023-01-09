x = float(input("Insira um número inteiro ou decimal: "))

arredondado = round(x)

if x == arredondado:
  print("Número inteiro")
else:
  print("Número decimal")