data = input("Insira seu nascimento: ")

if str(data[3:5]) == "01":
    mes = "janeiro"
elif str(data[3:5]) == "02":
    mes = "fevereiro"
elif str(data[3:5]) == "03":
    mes = "março"
elif str(data[3:5]) == "04":
    mes = "abril"
elif str(data[3:5]) == "05":
    mes = "maio"
elif str(data[3:5]) == "06":
    mes = "junho"
elif str(data[3:5]) == "07":
    mes = "julho"
elif str(data[3:5]) == "08":
    mes = "agosto"
elif str(data[3:5]) == "09":
    mes = "setembro"
elif str(data[3:5]) == "10":
    mes = "outubro"
elif str(data[3:5]) == "11":
    mes = "novembro"
elif str(data[3:5]) == "12":
    mes = "dezembro"

print(f"Você nasceu em {data[0:2]} de {mes} de {data[6:10]}.")