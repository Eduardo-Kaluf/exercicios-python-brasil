def conversor(x):
    convertido = int(x) / 1048576
    convertido = round(convertido, 2)
    return convertido

def percentual(x):
    convertido = (x * 100) / soma
    convertido = round(convertido, 2)
    return(convertido)

espaço_4 = []
espaço_3 = []
conteudos = []
espaço = []
nomes = []
nomes_2 = []
espaço_2 = []
porcentagem_ocupada = []
porcentagem_ocupada_2 = []
porcentagem_ocupada_3 = []
numeros = []
x = 0
arquivo = open("ex_2_dos_arquivos.txt", "r")
conteudo = arquivo.readlines()

for i in conteudo:
    i = i.replace("\n", "")
    conteudos.append(i)

y = len(conteudo)

while x < y:
    nomes.append(conteudos[x][0:15])
    espaço.append(conteudos[x][15:])
    x = x + 1
x = 0
for i in nomes:
    nomes_2.append(i)

while x < len(nomes_2):
    numeros.append(x + 1)
    x = x + 1

for i in espaço:
    z = i.strip()
    z = conversor(z)
    espaço_2.append(z)
soma = sum(espaço_2)
x = 0
while x < len(espaço_2):
    porcentagem_ocupada.append(percentual(espaço_2[x]))
    x = x + 1
x = 0

arquivo.close()

saida = open("relatório.txt", "w", encoding="utf-8")

while x < len(espaço_2):
    l = (str(espaço_2[x])).replace(".", ",")
    espaço_3.append(l)
    x = x + 1
x = 0
for i in espaço_3:
    while len(i) < 8:
        i = i + ' '
    espaço_4.append(i)

while x < len(porcentagem_ocupada):
    l = (str(porcentagem_ocupada[x])).replace(".", ",")
    porcentagem_ocupada_2.append(l)
    x = x + 1

for i in porcentagem_ocupada_2:
    while len(i) < 8:
        i = i + ' '
    porcentagem_ocupada_3.append(i)

media = soma / len(nomes_2)
media = round(media, 2)

saida.write("ACME Inc.               Uso do espaço em disco pelos usuários\n"
    "------------------------------------------------------------------------\n"
    "Nr.  Usuário        Espaço utilizado     % do uso\n\n"
    f"{numeros[0]}    {nomes_2[0]}{espaço_4[0]}" + " MB"f"          {porcentagem_ocupada_3[0]}" + "% \n"
    f"{numeros[1]}    {nomes_2[1]}{espaço_4[1]}" + " MB"f"          {porcentagem_ocupada_3[1]}" + "% \n"
    f"{numeros[2]}    {nomes_2[2]}{espaço_4[2]}" + " MB"f"          {porcentagem_ocupada_3[2]}" + "% \n"
    f"{numeros[3]}    {nomes_2[3]}{espaço_4[3]}" + " MB"f"          {porcentagem_ocupada_3[3]}" + "% \n"
    f"{numeros[4]}    {nomes_2[4]}{espaço_4[4]}" + " MB"f"          {porcentagem_ocupada_3[4]}" + "% \n"
    f"{numeros[5]}    {nomes_2[5]}{espaço_4[5]}" + " MB"f"          {porcentagem_ocupada_3[5]}" + "% \n\n"
    
    "Espaço total ocupado: " + f"{soma}" + " MB\n" 
    "Espaço médio ocupado: " + f"{media}" + " MB"
)
