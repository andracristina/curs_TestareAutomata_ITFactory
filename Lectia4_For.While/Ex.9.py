# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]

for numar in numere:
    if numar > max:
        max = numar

print(max)
