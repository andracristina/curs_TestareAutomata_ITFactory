'''
functie calculare impozit masina:
input: centimetri_cubi, este_hibrid
daca e hibrid, e 10, altfel sunt 3 categorii de taxe:
mai mic de 1300: 70,
mai mic de 2300:160
peste 2300: 900
'''

def calculare_impopzit(cc, este_hibrid):
    if este_hibrid == True:
        return 10
    elif cc < 1300:
        return 70
    elif cc < 2300:
        return 160
    elif cc > 2300:
        return 900


print(calculare_impopzit(1200,True))

