import operator

def porcentagem(todo, quantia):
    porcentagem = (100 * quantia) / todo
    porcentagem = round(porcentagem, 2)
    return(porcentagem)

sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = []
quantia = []
porcentagems = []
dic = {}
x = 0
voto = None


while voto != 0:
    voto = int(input("Insira seu voto: "))
    if voto < 0 or voto > 6:
        print("Inválido")
        continue
    votos.append(voto)

while x < 6:
    y = votos.count(x + 1)
    dic.update({x + 1: y})
    quantia.append(y)
    x = x + 1

total = sum(quantia)
max_key = max(dic.items(), key=operator.itemgetter(1))[0]
max_key = max_key - 1

x = 0
while x < 6:
    z = porcentagem(total, quantia[x])
    porcentagems.append(z)
    x = x + 1

print("\nSistema Operacional      Votos       %\n--------------------     -----     -----")

print(f"""Windows Server           {str(quantia[0]).ljust(10)}{porcentagems[0]}
Unix                     {str(quantia[1]).ljust(10)}{porcentagems[1]}
Linux                    {str(quantia[2]).ljust(10)}{porcentagems[2]}
Netware                  {str(quantia[3]).ljust(10)}{porcentagems[3]}
Mac OS                   {str(quantia[4]).ljust(10)}{porcentagems[4]}
Outro                    {str(quantia[5]).ljust(10)}{porcentagems[5]}
--------------------     -----     -----
Total                    {total}\n
O Sistema Operacional mais votado foi o {sistemas[max_key]}, com """ + 
f"""{quantia[max_key]} votos, correspondendo a {porcentagems[max_key]} % dos votos.""")
