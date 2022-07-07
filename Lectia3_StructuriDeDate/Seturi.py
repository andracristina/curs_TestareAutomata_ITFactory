# mai multe valori unice intr-o variabila
# nu sunt ordonate sau indexate
# len() pt a afla dimensiunea
# nu se poate schimba locatia elementelor
# putem adauga sau sterge elemente

vocale = {'a', 'e', 'i', 'o', 'u'}

# litera = input('Scrie o litera:')
# if litera.casefold() in vocale:
#     print('Este o vocala')
# else:
#     print('Nu este o vocala')


vocale.add('w') # adaugam o valoare
print(vocale)

set2 = {'mere', 'pere', 'castane', 'struguri'}
set3 = {'mere', 'struguri'}

res = set2.intersection(set3) # intersectia dintre seturi
print(res)

res = set2.union(set3) # se suprapun seturile
print(res)

print(set3.issubset(set2))   # boolean, se contine lista 3 in lista 2?
