x = 0
perguntas = ["Número 1: ", "Número 2: ", "Número 3: ", "Número 4: ", "Número 5: " ]
a = []

while x < len(perguntas):
    b = int(input(perguntas[x]))
    a.append(b)
    x = x + 1

print(max(a))
