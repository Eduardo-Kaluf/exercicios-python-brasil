salario = None
salarios = []
abonos = []

while 1:
    salario = float(input("Insira o salário: "))
    if salario == 0:
        break
    salarios.append(salario)
    if salario < 500:
        abono = 100
        abonos.append(abono)
    else:
        abono = salario * 0.2
        abonos.append(abono)

print("Projeção de Gastos com Abono\n============================\nSalário     -    Abono ")

x = 0

for i in salarios:
    salarios[x] = str(salarios[x]).ljust(8)
    print(f"R$ {salarios[x]} -    R$ {abonos[x]}")
    x = x + 1

print(f"""
Foram processados {len(salarios)} colaboradores
Total gasto com abonos: R$ {sum(abonos)}
Valor mínimo pago a {abonos.count(100)} colaboradores
Maior valor de abono pago: {max(abonos)}
""")
