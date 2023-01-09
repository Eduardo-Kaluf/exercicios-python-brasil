x =   ("""                    Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg """)

tipo_de_carne = input("Qual carne deseja? (F, A ou P) ").upper()
kg = float(input("Quantos kg? "))

if kg <= 5:
    F = 4.90
    A = 5.90
    P = 6.90
else:
    F = 5.80
    A = 6.80
    P = 7.80

if tipo_de_carne == F:
    preço = F * kg
elif tipo_de_carne == A:
    preço = A * kg
else:
    preço = P * kg

pagamento = input("Como deseja pagar? (Cartão ou Dinheiro) ").upper()

if pagamento == "CARTÃO":
    desconto = 0.05
    preço_desconto = (preço - (preço * desconto))
else:
    desconto = 0.00
    preço_desconto = preço

cumpom_fiscal = f"""Tipo = {tipo_de_carne}
Quantidade = {kg}
Preço total = {preço}
Tipo de pagamento = {pagamento}
Valor do desconto = {desconto}
Valor a pagar = {preço_desconto}
"""

print(cumpom_fiscal)