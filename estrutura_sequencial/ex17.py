
from math import ceil

area = float(input("Digite a area: "))

litros = area / 6

latas = ceil(litros / 18)
galoes = ceil(litros / 3.6)

eco_latas = litros // 18
eco_galoes = ceil(((litros % 18) / 3.6) * 1.1)

print(f"Preciso de {latas}, custando {latas*80}")
print(f"Preciso de {galoes}, custando {galoes*25}")
print(f"Preciso de {eco_latas} e {eco_galoes}, custando {(eco_latas*80) + (eco_galoes*25)}")
