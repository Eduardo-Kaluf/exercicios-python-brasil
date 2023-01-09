ano = int(input("Ano de contrato: "))
x = 1
total_de_anos = 2022 - ano
salario = 1000
porcentual = 0.015
while x < total_de_anos:
    porcentual = porcentual * x
    total = 1 + porcentual
    salario = salario * total
    x = x + 1

print(salario)
