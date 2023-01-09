"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

a = input("Telefonou para a vítima? ").upper()
b = input("Esteve no local do crime? ").upper()
c = input("Mora perto da vítima? ").upper()
d = input("Devia para a vítima? ").upper()
e = input("Já trabalhou com a vítima? ").upper()

"""lista_de_perguntas = [a, b, c, d, e]

if 2(vars) in lista_de_perguntas == "SIM":
  print("Suspeita")
elif 3 in lista_de_perguntas or 4 in lista_de_perguntas == "SIM":
  print("Cúmplice")
elif 5 in lista_de_perguntas == "SIM":
  print("Assasino")
else:
  print("Inocente")"""

if a == "SIM":
  valor_a = 1
else:
  valor_a = 0

if b == "SIM":
  valor_b = 1
else:
  valor_b = 0

if c == "SIM":
  valor_c = 1
else:
  valor_c = 0

if d == "SIM":
  valor_d = 1
else:
  valor_d = 0

if e == "SIM":
  valor_e = 1
else:
  valor_e = 0

valor_total = (valor_a + valor_b + valor_c + valor_d + valor_e)

if valor_total == 2:
  print("Suspeito")
elif valor_total == 3 or valor_total == 4:
  print("Cúmplice")
elif valor_total == 5:
  print("Assassino")
else:
  print("Inocente")