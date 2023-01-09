x = 0 
anos_e_temperaturas = []
messes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperarturas = []
while x < 12:
    temperatura = input("Insira a temperatura pro mês " + str(x + 1) + ": ")
    temperarturas.append(float(temperatura))
    anos_e_temperaturas.append(messes[x] + " - " + (temperatura))
    x = x + 1

media = sum(temperarturas) / len(temperarturas)

print(f"A média foi de: {media}")
print(anos_e_temperaturas)
