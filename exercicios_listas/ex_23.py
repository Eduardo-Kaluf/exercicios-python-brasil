def conversor(x):
    convertido = int(x) / 1048576
    convertido = round(convertido, 2)
    return convertido

def percentual(x):
    convertido = (x * 100) / soma
    convertido = round(convertido, 2)
    return(convertido)

def virgula(x):
    x = str(x).replace(".", ",")
    return(x)

espaço = []
nomes = []
numeros = []
x = 0

arquivo = open("ex_2_dos_arquivos.txt", "r")

conteudo = arquivo.readlines()

for i in conteudo:
    i = i.replace("\n", "")
    nomes.append(i[0:15])
    espaço.append(int(i[15:]))
    numeros.append(x + 1)
    x = x + 1

soma = sum(espaço)

arquivo.close()

saida = open("relatório.txt", "w", encoding="utf-8")

saida.write("ACME Inc.               Uso do espaço em disco pelos usuários\n"
    "------------------------------------------------------------------------\n"
    "Nr.  Usuário        Espaço utilizado     % do uso\n\n")

x = 0

for i in conteudo:
    numero = str(numeros[x]).ljust(5)
    nome = str(nomes[x]).ljust(8)
    mb = virgula(str(conversor(espaço[x])).ljust(10))
    porcentagem = virgula(str(percentual(espaço[x])).rjust(14))
    saida.write(f"{numero}{nome}{mb}MB{porcentagem} %\n")
    x = x + 1

saida.write(f"\nEspaço total ocupado: {virgula(conversor(soma))}\nEspaço médio ocupado: {virgula(round(conversor(soma) / len(conteudo), 2))}")
