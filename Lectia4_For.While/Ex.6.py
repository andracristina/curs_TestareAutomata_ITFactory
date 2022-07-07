# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

print(pret_masini.items())

for key, value in pret_masini.items():    # iteram prin dict, fiecare item
    print(key, ' : ', value)

for key, value in pret_masini.items():
    if value <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {key}')
