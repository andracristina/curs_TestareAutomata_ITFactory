#  Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def comparatie(x,y):
    if x > y:
        print('Primul numar x este mai mare decat al doilea nr y')
    elif x < y:
        print('Al doilea nr y este mai mare decat primul nr x')
    elif x == y:
        print('Numerele sunt egale')

print(comparatie(-7,7))
