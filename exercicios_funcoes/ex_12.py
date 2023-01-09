import random

palavra = input("Insira uma palavra: ").upper()

def embaralha(x):
    y = list(x)
    random.shuffle(y)
    y = "".join(y)
    return(y)

resultado = embaralha(palavra)

print(resultado)
