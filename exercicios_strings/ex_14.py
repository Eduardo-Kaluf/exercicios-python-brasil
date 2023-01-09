
palavra = input("Insira a palavra leet: ")

dic = {
"l": "1", 
"e": "3",
"t": "7"
}

for letra in palavra:
    if letra in dic.keys():
        palavra = palavra.replace(letra, dic[letra])

print(palavra)
