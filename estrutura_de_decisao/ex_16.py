print("Calculadora de equações do segundo grau! ")

a = float(input("insira o valor de a: "))

if a == 0:
  print("Não é uma equação de segundo grau")
  exit()

b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
  print("Não possue soluções reais")
  exit()

resultado_1 = (- b + delta ** 0.5) / 2 * a
resultado_2 = (- b - delta ** 0.5) / 2 * a

if delta == 0:
  print("Possue apenas 1 resultado: ")
  print(resultado_1)
else:
  print("A equação possue 2 resultados: ")
  print(resultado_1, resultado_2)