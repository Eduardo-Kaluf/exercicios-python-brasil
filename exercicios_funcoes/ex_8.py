numero = (input("Insira um número inteiro: "))

def contador(x):
    lista = [i for i in x]
    return len(lista)

quantia = contador(numero)

print(quantia)
