print("Insira uma data no formato aa/mm/aaaa: ")

dia = int(input("Insira o dia: "))
mês = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))

inválido = ("Data inválida")

if dia > 31 or dia < 0:
  print(inválido)
elif dia == 28 and mês != 2:
  print(inválido)
elif mês > 12 or mês < 1:
  print(inválido)
else:
  print("Data válida!")