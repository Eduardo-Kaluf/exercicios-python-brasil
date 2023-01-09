x = float(input("Insira sua primeira nota: "))
y = float(input("Insira sua segunda nota: "))

média = ((x + y) / 2)

if média >= 9:
  conceito = ("A")
elif média >= 7.5 and média < 9:
  conceito = ("B")
elif média >= 6 and média <7.5:
  conceito = ("C")
elif média >= 4 and média < 6:
  conceito = ("D")
else:
  conceito = ("E")

lista_de_letras = ["A", "B", "C"]

if conceito in lista_de_letras:
  aprovação = ("APROVADO")
else:
  aprovação = ("REPROVADO")



Resultado = f"Suas notas foram {x} e {y}, sendo assim sua média é {média}, seu conceito foi {conceito} e você está {aprovação}"

print(Resultado)