valor_do_item = float(input("Insira o valor do produto: "))
taxa = float(input("Insira a taxa de imposto: "))

def soma_imposto(x, y):
    taxa_imposto = x
    altera = x * y
    return taxa_imposto, altera

imposto = soma_imposto(valor_do_item, taxa)

print(str(imposto))
