telefone = input("Insira o número de telefone: ")

print(f"Telefone: {telefone}")

if "-" in telefone and len(telefone) == 8:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    telefone = "3" + telefone
elif "-" not in telefone and len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    telefone = "3" + telefone[0:3] + "-" + telefone[3:]
else:
    print("Telefone válido")

print(telefone)
