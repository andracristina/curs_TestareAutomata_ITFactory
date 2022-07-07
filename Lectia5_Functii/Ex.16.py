# 16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}



def nr_cumone(lista1, lista2):
    raspuns = set()
    for nr in lista1:
        if nr in lista2:
            raspuns.add(nr)
    return raspuns

list1 = [1, 1, 2, 3, 6, 8, 0, 2, 4, 7, 55, 67, 100, 200, 230, 1243, 88]
list2 = [2, 2, 3, 4, 8, 0, 4, 4, 7, 99, 6, 88]

print(nr_cumone(list1,list2))

#print(nr_cumone([1,2,3,4,5],[3,4,5,6,7,8]))


