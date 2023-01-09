frase = input("Insira uma frase: ").upper()

vogais_lista = ["A", "E", "I", "O", "U"]

espaços = frase.count(" ")

vogais = 0

for i in vogais_lista:
    vogais = vogais + frase.count(i)

print(f"A quantia de espaçoes é {espaços}")
print(f"A quantia de vogais é {vogais}")
