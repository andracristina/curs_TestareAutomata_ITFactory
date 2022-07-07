# in python o lista poate cotine valori de mai multe tipuri
# mai multe valori intr-o sg variabila
# fiecare element are un index, incepe de la 0
# lista este ordonata, fiecare element nou se va adauga la final
# lista este mutabila - Putem edita elementele din lista
# functia len ne da lungimea listei

nume = 'Alexandru'
nume_as_list = ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'r', 'u']

print(nume)
print(nume_as_list)

print(nume[2])
print(nume_as_list[2])

print(nume_as_list [0:4:2])

nume_as_list.append('le') # adaugam la capatul listei

nume_as_list.insert(4, 10) # adaugam la indexul 4 valoarea 10
print(nume_as_list)

nume_as_list.remove('x') # scoate prima incidenta unde gaseste x, nu pe toate
print(nume_as_list)

nume_as_list.pop() # default se scoate ultima valoare din lista
print(nume_as_list)
print(nume_as_list.pop(0))
print(nume_as_list)

print(nume_as_list.count('e'))

print(nume_as_list.count('x'))


nume_as_list2 = ['i', 'o', 'n']
print(nume_as_list2)


nume_as_list.extend(nume_as_list2) # adaugam o lista noua la prima lista
print(nume_as_list)
#
# nume_as_list.clear() # sterg lista
# print(nume_as_list)

tabla_sah = [   # lista in lista, elemebte diferite pe randuri
    [1,0,1,0,1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
]

print(len(tabla_sah))
print(len(tabla_sah[0]))