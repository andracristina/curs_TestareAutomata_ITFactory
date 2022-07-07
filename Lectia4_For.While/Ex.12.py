#Ordonati crescator lista fara sa folositi sort

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_ordonata = []

while alte_numere:
    min = alte_numere[0]
    for numar in alte_numere:
        if numar < min:
            min = numar
    lista_ordonata.append(min)
    alte_numere.remove(min)

print(lista_ordonata)
