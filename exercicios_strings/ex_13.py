from random import randint
import os

def escaralhador(palavra):
    embaralhada = []
    for i in palavra:
        embaralhada.insert(randint(0, len(palavra)), i)
    embaralhada = "".join(embaralhada)
    return(embaralhada)

BASE = os.getcwd()
arquivo = open(os.path.join(f"{BASE}", "arquivos", "palavras.txt"), "r")
palavras = arquivo.readlines()
palavra = palavras[randint(0, len(palavras))].replace("\n", "")

arquivo.close()

erro = 0

embaralhada = escaralhador(palavra)

print(embaralhada)

while 1:
    resposta = input("Insira sua resposta: ")
    if resposta == palavra:
        print(palavra + "\nGanhou")
        break
    else:
        erro = erro + 1
        print(f"Erros: {erro}")
    if erro >= 6:
        print("Você perdeu")
        break
