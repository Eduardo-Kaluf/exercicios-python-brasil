frase_1 = input("Insira a primeira string: ")
frase_2 = input("Insira a segunda string: ")

print(f"Frase 1: {frase_1}\nFrase 2: {frase_2}\nTamanho de {frase_1} é {len(frase_1)} caracteres\nTamanho de {frase_2} é {len(frase_2)} caracteres")

if frase_1 == frase_2:
    print("São iguais")
else:
    print("São diferentes")
