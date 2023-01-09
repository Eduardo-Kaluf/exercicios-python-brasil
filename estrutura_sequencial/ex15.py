Ganho = float(input("Quanto você ganha por hora? "))
Horas = float(input("Quantas horas você trabalha por mês? "))

Bruto = (Ganho * Horas)
IR = (Bruto * 0.11)
INSS = (Bruto * 0.08)
Sindicato = (Bruto * 0.05)
Liquido = (((((Bruto - IR) - INSS) - Sindicato)))

Resultado = f"Seu salário bruto é {Bruto}, o desconto pelo IR INSS e pelo Sindicato são respectivamente iguais à {IR}, {INSS}, {Sindicato}"

print(Resultado)
