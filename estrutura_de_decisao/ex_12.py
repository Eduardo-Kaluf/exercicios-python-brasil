from tkinter import N


ganho_por_hora = float(input("Quanto você ganha por hora? "))
total_de_horas = float(input("Quantas horas você trabalha por mês? "))

salario = (ganho_por_hora * total_de_horas)

if salario <= 900:
  IR = 1
elif salario > 900 and salario <= 1500:
  IR = 0.05
elif salario > 1500 and salario <= 2500:
  IR = 0.10
else:
  IR = 0.20

desconto_IR = IR * salario

sindicato = (salario * 0.03)

FGTS = (salario * 0.11)

total_de_descontos = (sindicato + desconto_IR)

liquido = (salario - total_de_descontos)

Resultado = (f"Salário bruto: ({ganho_por_hora} * {total_de_horas}) : R${salario} \n (-) IR  ({IR}) : {desconto_IR} \n (-) INSS (0.03) : R$ {sindicato} \n FGTS (0.11) : R$ {FGTS} \n Total de descontos: R${total_de_descontos} \n Salário liquido: R$: {liquido}")

print(Resultado)