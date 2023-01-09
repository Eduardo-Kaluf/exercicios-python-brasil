veiculos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
km_por_l = [7, 10, 12.5, 9, 14.5]
menor_consumo = 100000
x = 0

print("Relatório Final")

for i in veiculos:
    gasto_de_l = round(1000 / km_por_l[x], 2)
    if gasto_de_l < menor_consumo:
        menor_consumo = gasto_de_l
        veiculo_economico = veiculos[x]
    custo = round(2.25 * gasto_de_l, 2)
    print(f"{x + 1} - {veiculos[x].ljust(10)} - {str(km_por_l[x]).ljust(7)} - {str(gasto_de_l).ljust(9) + 'litros'.ljust(8)} - R$ {custo}")
    x = x + 1

print(f"O menor consumo é do {veiculo_economico}")
