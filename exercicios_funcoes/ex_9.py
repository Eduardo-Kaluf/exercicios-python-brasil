numero = (input("Insira um número inteiro: "))

def reverso(x):
    lista = [i for i in x]
    y = -1
    lista_2 = []
    z = 0
    while z < len(lista):
        lista_2.append((lista[y]))
        y = y - 1
        z = z + 1
    lista_2 = "".join(lista_2)
    return (lista_2)

resultado = reverso(numero)

print(resultado)
