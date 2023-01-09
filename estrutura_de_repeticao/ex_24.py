from statistics import mean

total_notas = int(input("Total de notas: "))
x = 0
notas = []
while x < total_notas:
    nota = float(input("Insira sua nota de número " + str(x + 1) + ": "))
    notas.append(nota)
    x = x + 1

print(mean(notas))
