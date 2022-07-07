masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while


for masina in range(len(masini)):
    print(f'Masina mea preferata este {masini[masina]}')

for masina in masini:
    print(f'Masina mea preferata este {masina}')

iterator = 0
while iterator < len(masini):
    print(f'Masina mea preferata este {masini[iterator]}')
    iterator +=1


