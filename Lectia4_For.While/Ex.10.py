# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_noua = []

for i in range(len(numere)):
    numar = numere[i]
    if numar > 0:
        numar = -1*numar
        lista_noua.append(numar)
print(lista_noua)


