vetor = []

while len(vetor) < 10:
    letra = input("Insira uma letra: ")
    vetor.append(letra)

vogais = ["a", "e", "i", "o", "u"]

consoantes = [c for c in vetor if c not in vogais]

print(len(consoantes))
