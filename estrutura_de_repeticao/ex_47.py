nome = input("Insira o nome do atleta: ")
notas = []
x = 0
while x < 7:
    nota = float(input("Insira a nota: "))
    notas.append(nota)
    x = x + 1
x = 0
print(f"\nAtleta: {nome}")
while x < 7:
    print(f"Nota: {notas[x]}")
    x = x + 1

melhor = max(notas)
pior = min(notas)
media = (sum(notas) - (melhor + pior)) / 5
notas.remove(melhor)
notas.remove(pior)

print("\nResultado final:")
print(f"Atleta: {nome}")
print(f"Melhor nota: {melhor}")
print(f"Pior nota: {pior}")
print(f"Média: {media}")
