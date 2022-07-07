# mai multe valori imutabile intr-o variabila
# sunt ordonate, incep de la index 0
# valorile odata definite, asa raman; nu mai pot adauga sau sterge valori
# accepta valori duplicate
# len() pt a det dimensiunea

tuple = ('banane', 'piersici', 'mere', 312, True, 2.3411)

print(len(tuple)) # dimensiunea

print(tuple[4]) # index

print(tuple[2:3])   # slicing

print(type(tuple))

camera_hotel = (1,2,3,4,5,2)   # acestea sunt valorile, nu pot fi modificate

print(camera_hotel.__add__(tuple))  # putem sa concatenam 2 tupleuri