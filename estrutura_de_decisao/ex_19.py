x = int(input("Insira um número menor que 1000: "))

if x >= 1000:
  exit()

unidade = x % 10

print(unidade)


if x > 9:
  dezena = (((x - unidade) / 10) % 10)
  print(dezena)


if x > 99:
  centena = ((((x - unidade) / 10) - dezena) / 10)
  print(centena)

