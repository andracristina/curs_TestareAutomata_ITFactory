""" 1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
"""

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

print(len(note_muzicale))
note_muzicale = note_muzicale[::-1]
print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)


# 2. De cate ori apare ‘do’?

print(note_muzicale.count('do'))

# 3.
# Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# lista1.extend(lista2)
# print(lista1)

lista3 = lista1 + lista2
print(lista3)


# 4. # Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.extend(lista2)
print(lista1)

lista1.sort(reverse=True)
print(lista1)

lista1.remove(0)
print(lista1)

# 5. Folosind un if verificati lista generata la ex3 si afisati daca Lista este goala sau  Lista nu este goala

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.extend(lista2)
print(lista1)

lista1.sort(reverse=True)
print(lista1)

lista1.remove(0)
print(lista1)

#lista1.clear()

if len(lista1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')


# 6. Folositi o functie care sa stearga lista de la ex3
lista1.clear()
print(lista1)


# 7. Copy paste la ex 5. Verificati inca o data.Acum ar trebui sa se afiseze ca lista e goala

if len(lista1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

#8. # Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(dict1.items())

# 9. Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(dict1['Ana'])

print('Ana a luat nota ' + str(dict1['Ana']))
print('Gigel a luat nota ' + str(dict1['Gigel']))
print('Dorel a luat nota ' + str(dict1['Dorel']))


# 10.
# Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

dict1['Dorel'] = 6

print(dict1)

# 11.
# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

dict1.pop('Gigel')
print(dict1)

dict1.update({'Ionica': 9})
print(dict1)

# 12.
# Set
zile_sapt = {'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt.add('luni')
print(zile_sapt)


# 13.
# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

# 14. Afisati diferentele dintre aceste 2 seturi

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

print(zile_sapt.difference(weekend))

# 15. Afisati diferentele dintre aceste 2 seturi

print(zile_sapt.intersection(weekend))



# 16. # Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori
#
# Google search hint
# “how to check if item is in list python”
#
# """

echipa = {'j1', 'j2', 'j3', 'j4', 'j5'} # set - acelasi jucator nu poate fi de 2 ori pe teren
schimbari_max = 3
schimbari_efectuate = 1
schimbari_ramase  = schimbari_max - schimbari_efectuate
jucator_in = 'j7'
jucator_out = 'j1'

if jucator_out in echipa and schimbari_ramase > 0: # sau if jucator_out in echipa
    if jucator_in in echipa:
        print('Jucatorul este deja pe teren!')
    else: # cazul valid
        echipa.remove(jucator_out) # scoatem jucatorul
        echipa.add(jucator_in) # introducem jucatorul nou
        schimbari_ramase = schimbari_ramase - 1 # contorizam schimbarea
        print(f'A intrat jucatorul {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari. Echipa noua este {echipa}')
else:
    if schimbari_efectuate == schimbari_max:
        print(f'Nu se poate efectua schimbare, nu mai aveti schimbari ramase')
    else:
        print(f'Nu se poate efectua schimbarea, {jucator_out} nu este pe teren')


