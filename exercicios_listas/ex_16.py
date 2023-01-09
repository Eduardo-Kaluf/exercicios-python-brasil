a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0

while 1:
    bruto = (input("Salario bruto: ")).upper()
    if bruto == "QUEBRAR":
        break
    salario = 200 + (int(bruto) * 0.09)
    if salario > 199 and salario < 300:
        a = a + 1
    elif salario > 299 and salario < 400:
        b = b + 1
    elif salario > 399 and salario < 500:
        c = c + 1
    elif salario > 499 and salario < 600:
        d = d + 1
    elif salario > 599 and salario < 700:
        e = e + 1
    elif salario > 699 and salario < 800:
        f = f + 1
    elif salario > 799 and salario < 900:
        g = g + 1
    elif salario > 899 and salario < 1000:
        h = h + 1
    else:
        i = i + 1

lista = [a, b, c, d, e, f, g, h, i]

print(lista)
