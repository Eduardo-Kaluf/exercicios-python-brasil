x = 0
alturas = {}
while x < 10:
    número = int(input("Insira seu número: "))
    altura = float(input("Insira sua altura: "))
    alturas.update({número: altura})
    x = x + 1

maximo, minimo = max(alturas.values()), min(alturas.values())

id_max = alturas.get(maximo)

id_min = alturas.get(minimo)

resultado = f"O aluno com o número {id_max} é o mais alto com a altura de {maximo}, \n E o aluno com o número {id_min} é o mais baixo com a altura de {minimo}"

print(resultado)
