# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila

# o variabile reprezinta un spatiu de memorie in care se salveaza date

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool

marca = 'Mercedes' #string
an = 2012 #int
pret = 6367.97 #float
cutie_automata = True #bool

# 3. Utilizat functia type pentru a verifica daca au tipul de date asteptat

print(type(marca))
print(type(an))
print(type(pret))
print(type(cutie_automata))

# 4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere). Verificati tipul acesteia

pret = round(pret)
print(pret)

# 5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. (rezolvati nepotrivirile de tip prin ce modalitate doriti)

# 6. citeste de la tastatura numele. citeste de la tastatura prenumele. afiseaza 'Numele complet are x caractere'

nume = input('Numele este: ')
prenume = input('Prenumele este: ')

print(f'Numele complet are {len(nume) + len(prenume)} caractere')

# 7.citeste de la tastatura lungimea. citeste de la tastatura latimea.  afiseaza 'Aria dreptunghiului este x'

lungimea = int(input('Lungimea este: '))
latimea = int(input('Latimea este: '))
aria = lungimea * latimea

print(f'Aria dreptunghiului este {aria}')

# 8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', cititi de la tastatura un int x. Afiseaza stringul fara ultimele x caractere

propozitie = 'Coral is either the stupidest animal or the smartest rock'
cate_caractere = int(input('Cate caractere doresi sa stergi?'))

print(propozitie[0:-cate_caractere])

# 9. acelasi string. Declara un string nou care sa fie format din primele 5 caractere + ultimele 5

print(len(propozitie))
prpozitie_noua = propozitie[0:4] + propozitie[52:57]

print(prpozitie_noua)

# 10. acelasi string afisati de cate ori apare cuvantul 'the'
print(propozitie.count(' the'))



# 12. acelasi string. salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock.  (hint: este o functie care te ajuta sa faci asta)
# # folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant.  output: 'Coral is either the stupidest animal or the smartest'

index = propozitie.index('rock')
print(index)
print(propozitie[0:53])

# 13. citeste de la tastatura un string. verifica daca primul si ultimul caracter sunt la fel. se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive 'apA' e acceptat

cuvant = input('Scrie un string: ')

assert cuvant.casefold()[0] == cuvant.casefold()[-1]
print('prima si ultima litera sunt la fel')


""" assert cuvant.casefold()[0] != cuvant.casefold()[-1]
print('prima si ultima litera sunt diferite')
"""

# 14. avand stringul '0123456789'. afisati doar numerele pare. acum afisati doar numerele impare. (hint: folositi slicing, controlati din pas)
numere = '0123456789'
print(numere.index('9'))
print(numere[0:-1:2])

# 15. acelasi string de mai sus. folositi un assert ca sa verificati daca acest string contine doar numere. hint: merge cu slicing?
# probabil ca nu... ce mai stim atunci legat de string? poate gasim o functie ajutatoare

propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert propozitie.isnumeric()


# 16. citeste de la tastatura un string de dimensiune impara. afiseaza caracterul din mijloc

un_cuvant = (input('Srie un cuvant de dimensiune impara: '))

def middle_char(un_cuvant):
    return un_cuvant[(len(un_cuvant)-1)//2:(len(un_cuvant)+2)//2]

print('Caracterul din mijloc este ' + middle_char(un_cuvant))




# 17. Folosind assert, verificati daca un string este palindrom

palindrom = input('Scrieti un palindrom: ')

reversul = palindrom[::-1]

assert palindrom == reversul
print('Acest cuvant este un palindrom')

""" assert palindrom != reversul
print('Acest cuvant NU este un palindrom')
"""


# 18. folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala') si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare
# taking two inputs at a time
a, b = input('scrie doua cuvinte: ').split()
print('Prima variabila este {} iar a doua este {}'.format(a,b))



# 19. citeste un string de la tastatura (eg: alabala portocala). salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2
#  stringuri diferite). Capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter.  => alAbAlA portocAla

un_string = input('Scrie ceva: ')
char1 = un_string[0]


# 20. citeste un user de la tastatura. citeste o parola. afiseaza: 'Parola pt user x este ***** si are x caractere'. ***** se va calcula dinamic,
# indiferent de dimensiunea parolei, trebuie sa afiseze corect: eg: parola abc => ***, parola abcd => ****

user = input('Introduceti user: ')
parola = input('Introduceti parola: ')
nr_car = len(parola)
print(f'Parola pentru {user} este {parola} si are {nr_car} caractere')