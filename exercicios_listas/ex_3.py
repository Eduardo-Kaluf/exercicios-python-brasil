from statistics import mean

notas = []
while len(notas) < 4:
    nota = int(input("Insira sua nota: "))
    notas.append(nota)

print(notas)
print(mean(notas))
