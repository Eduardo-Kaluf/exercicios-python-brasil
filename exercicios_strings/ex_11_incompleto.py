import os
from random import randint

base = os.getcwd()

arquivo = open(os.path.join(f"{base}", "Aulas_de_Python", "arquivos", "ex_da_forca.txt"), "r")

conteudo = arquivo.readlines()

arquivo.close()

x = 1
letras = []
palavras = []

for i in conteudo:
    i = i.strip()
    palavras.append(i)

palavra_forca = palavras[randint(0, len(palavras) - 1)]
for i in palavra_forca:
    letras.append(i)

resposta = "_" * len(palavra_forca)

while x < 8:
    letra = input("Digite uma letra: ")
    letras.count(letras)
    if letra in letras:
        local = letras.index(letra)
        resposta = resposta[:local] + letra + resposta[local+1:]
        print(resposta)
        if "_" not in resposta:
            print("Você Ganhou!!! (:")
            exit()
    else:
        print(f"Você errou pela {x}ª vez. Tente de novo!")
        x = x + 1

(print("Voce perdeu ):"))

#Está certo porem não funciona com palavras que tenham letras repitidas
