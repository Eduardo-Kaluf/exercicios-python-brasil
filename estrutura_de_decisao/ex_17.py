#Ano bissexto
x = int(input("Insira um ano: "))

divisão_1 = x % 4

if divisão_1 != 0:
  print("Não é bissexto!")
  exit()

divisão_2 = x % 100

if divisão_2 != 0:
  print("É bissexto!")
  exit()

divisão_3 = x % 400

if divisão_3 == 0:
  print("É bissexto!")
else:
  print("Não é bissexto!")