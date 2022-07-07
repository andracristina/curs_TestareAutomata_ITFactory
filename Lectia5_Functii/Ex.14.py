# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele

def max(a,b,c):
    if a > b and a > c:
        largest = a
        return a
    elif b > a and b > c:
        largest = b
        return b
    elif c > a and c > b:
        largest = c
        return c



print(max(7,74,90))