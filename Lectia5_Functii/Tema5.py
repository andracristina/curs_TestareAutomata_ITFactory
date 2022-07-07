# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def suma(a,b):
    return a+b

print(suma(4,7))

#2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

print(par_impar(191))

#  3 Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

def car_nume(nume, prenume, nume_mijlociu):
        return len(nume) + len(prenume) +len(nume_mijlociu)

print(car_nume('Andra', 'I', 'L'))

#