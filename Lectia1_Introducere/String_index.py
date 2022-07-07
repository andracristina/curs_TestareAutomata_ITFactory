# functia lenght
nume = 'bar!1'
print(len(nume))

# slicing   -   aflam un caracter dintr-un string; indexul intre [];
print(nume[1])

print(nume[0:3])

print(nume[::-1])  # intoarce caracterele de la cap la coada

print(nume.lower())
print(nume.upper())


if nume.isalpha():
    print('sunt doar litere')