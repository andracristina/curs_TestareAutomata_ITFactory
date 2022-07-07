""""
b. Usor spre Mediu (obligatoriu)
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int

1.
Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else

"""

# un IF ELSE reprezinta o bucata de cod care se executa doar atunci cand este indeplinita (True) conditia definita in IF.
# Daca nici una dintre conditiile IF declarate nu este indeplinita, se executa codul din ELSE.

# 2. Verifica si afiseaza daca x este numar natural sau nu

x = int(input('Introduceti un nr: '))

if x > 0:
    print('{x} este un nr natural')
else:
    print('{x} nu este un nr natural')

#3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input('Introduceti un numar: '))

if x < 0:
    print('Acesta este un nr negativ')
elif x == 0:
    print('Acest nr este neutru')
else:
    print('Acesta este un nr pozitiv')

# 4. Verifica si afiseaza daca x este intre -2 si 13

x = int(input('Introduceti un numar: '))

if - 2 < x < 13:
    print('Nr introdus este intre -2 si 13')
else:
    print('Mai incearca2')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

x = 9
y = 7

if x - y < 5:
    print('diferenta dintre x si y este mai mica de 5')
else:
    print('diferenta dintre x si y este mai mare de 5')

# 6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('Introduceti un numar: '))

if not 5 < x < 27:
    print('x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')

# 7.x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

x = 2
y = 9

if x == y:
    print('x si y sunt egale')
elif x > y:
    print('x e mai mare decat y')
else:
    print('y e mai mare decat x')

# 8.  X, y, z - laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

x = int(input('Introduceti lungimea primei laturi: '))
y = int(input('Introduceti lungimea celei de-a doua laturi: '))
z = int(input('Introduceti lungimea celei de-a treia laturi: '))

if x == y == z:
    print('Triunghiul este echilateral.')
elif x == y or x == z or y == z:
    print('Triunghiul este isoscel.')
else:
    print('Triunghiul este oarecare.')


# 9. Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu

litera = input('Scrie o litera: ')

if(litera == 'A' or litera =='a' or litera == 'E' or litera == 'e' or litera == 'I' or
        litera == 'i' or litera == 'O' or litera == 'o' or litera == 'U' or litera == 'u'):
    print('Litera este o vocala')
else:
    print('Litera este o consoana')


"""
10. Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

nota = int(input('Introduceti nota: '))
if nota > 10 or nota < 1:
    print('Scrieti o nota valida!')
elif nota == 9 or nota == 10:
    nota = 'A'
    print(f'Nota este {nota}')
elif nota == 8:
    nota = 'B'
    print(f'Nota este {nota}')
elif nota == 7:
    nota = 'C'
    print(f'Nota este {nota}')
elif nota == 6:
    nota = 'D'
    print(f'Nota este {nota}')
elif nota == 5 or nota == 4:
    nota = 'E'
    print(f'Nota este {nota}')
elif nota <= 4:
    nota = 'F'
    print(f'Nota este {nota}')


#11.Verifica daca x are minim 4 cifre (x e int); (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = int(input('Introduceti un numar: '))

if x >= 1000 or x <= -1000:
    print('Numaul are minim 4 cifre')
else:
    print('Numarul are mai putin de 4 cifre')


#12. Verifica daca x are exact 6 cifre

x = int(input('Scrie un numar: '))

if x >= 100000 or x <= -100000:
    print('Nr are 6 cifre')
else:
    print('Nr NU are 6 cifre')



# 13. Verifica daca x este numar par sau impar (x e int)

x = int(input('Scrieti un numar: '))

if x % 2 == 0:
    print('Numarul este par')
else:
    print('Nr este impar')


#c. Optionale (may need google)

# 14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?

x = int(input(' x = '))
y = int(input(' y = '))
z = int(input(' z = '))

if x == y == z:
    print('Cele 3 numere sunt egale')
elif x > y or x > z:
    print('X este cel mai mare')
    if x == y or x == z:
        print('Nr cel mai mare apare de 2 ori')
elif y > x or y > z:
    print('Y este cel mai mare')
    if y == x or y == z:
        print('Nr cel mai mare apare de 2 ori')
elif z > y or z > z:
    print('Z este cel mai mare')
    if z == x or z == y:
        print('Nr cel mai mare apare de 2 ori')


# 15.
# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu


x = int(input('Primul unghi: '))
y = int(input('Al doilea unghi: '))
z = int(input('Al treilea unghi: '))

if x < 0 or y < 0 or z < 0:
    print('Introduceti dimensiunea corecta!')
elif x + y + z > 180:
    print('Triunghiul nu este valid, suma unghiurilor este > 180 grade')
else:
    print('Triunghiul este valid')


"""
Bonus la cerere:
16.
Verificare imbarcare persoane
Tineti urmatoarele date
Varsta
Insotit de mama
Insotit de tata
Pasaport
Act permisiune mama
Act permisiune tata

Conditii de imbarcare
Daca pers are varsta peste 18 ani si are pasaport
Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

Aici vreau sa testati codul cu toate variantele posibile
Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results

Ex:
Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
Etc
"""

varsta = 5
pasaport = True
mama = False
tata = True
acord_mama = True
acord_tata = False

if pasaport == False: # nu avem pasaport
    print('Nu te poti imbarca fara pasaport!')
else: # avem pasaport
    print('OK, ai pasaport!')
    if varsta >= 18:
        print('Calatorie placuta!')
    else:
        print('Sunt minor, am pasaport')
        if mama == True and tata == True:
            print('Poti calatori cu parintii ti!')
        elif mama == False and tata == True and acord_mama == True:
            print('Poti calatori cu tatal tau')
        elif tata == False and mama == True and acord_tata == True:
            print('Poti calatori cu mama ta')
        else:
            print('Nu te poti imbarca!')

#
# 17. Joc ghicit zarul
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# Luati un nr ghicit de la utilizator
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y


import random
dice_roll = random.randint(1,6)


nr_ales = int(input('Ghiceste zarul: '))

if nr_ales > 6 or nr_ales < 1:
    print('Alege un nr intre 1 si 6!')

elif nr_ales == dice_roll:
    print(f'Ai ghicit. Felicitari? Ai ales {nr_ales} si zarul a fost {dice_roll}')
elif nr_ales > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {nr_ales} dar a fost {dice_roll}')
else:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {nr_ales} dar a fost {dice_roll}')

