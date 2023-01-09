cpf = input("Insira seu CPF: ")

if len(cpf) < 14:
    print("CPF inválido")
    exit()

cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

for i in cpf:
    if i.isnumeric():
        continue
    else:
        print("CPF inválido")
        exit()

print("CPF Válido")
