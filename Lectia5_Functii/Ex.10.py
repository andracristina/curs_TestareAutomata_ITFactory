# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def control_set(x):
    un_set = {1,2,3,4,5,8}
    if x not in un_set:
        un_set.add(x)
        print('am adaugat numarul nou in set')
     #   print(un_set)
        return True

    else:
        print(' nu am adaugat numarul in set. Acesta exista deja')
       # print(un_set)
        return False


print(control_set(8))
