Turno = (input("Qual turno você estuda? (Insira M, T ou N) ")).upper()


# if Turno != ("M") or ("T") or ("N"):
# Turno = ("invalido") 


if Turno == ("M"):
  print("Bom Dia!")
elif Turno == ("T"):
  print("Boa tarde!")
elif Turno == ("N"):
  print("Boa noite!")
else:
  print("Valor inválido")
