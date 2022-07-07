def media(a,b,c): # asa se scrie o functie; repetitiva, nun tb sa scriem de mai multe ori acelasi cod
    return (a+b+c)/3

print(media(1,2,3))

def say_hi():   # cea mai simpla functie; are nevoie de def si () pt a stii ca e functie;
    print('Hi!') # aceasta este actiunea asociata functiei; se repeta de cate ori apelam functia; functia asta nu ne ofera un REZULTAT care sa poata fi salvat intr-o variabila

say_hi()
say_hi()
say_hi()

x = say_hi() # asta ar insemna ca functia ne-ar da un raspuns, ceea ce aici nu se intampla; este necesar RETURN
print(x)

# functie cu parametri - datele de intrare in functie; sunt initializati la apelarea functie; sunt optionali
#ex. user - spunem Hi, numele + prenumele ( 0 --> oricati parametri)

def say_hi(nume, prenume):
    print(f'Hi, {nume} {prenume}')

say_hi('ion', 'li')
say_hi('ioana', 'li')

# ce este un RETURN
# se obtine atunci cand functia ne da si un raspuns (output); e optional, poate fi orice tip de date

#input de 3 numere
#vrem un set

def make_set(n1,n2,n3):
    r = set()
    r.add(n1)
    r.add(n2)
    r.add(n3)
    return r

set1 = make_set(1,2,3)   # nu printeaza! # in debug se vede doar daca salvam returnul intr-o variabila; altfel se executa dar nu 'vedem'
set2 = make_set(1,2,2)

print(make_set(1,2,3))
print(make_set(1,2,2))   # IN SET NU SE ADMIT DUPLICATE !!!

#cand apelez functia trebuie sa vizualizez deja rezultatul, astfel pot utiliza toate metodele care se pot aplica pe tipul de date din raspun
print(make_set(1,2,3).intersection(make_set(2,3,4)))   # pot aplica metode direct la functie; functia poate fi un parametru


#functie cu return dar fara parametri


