# 17. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida



def reducere(pret, procent_reducere):
    if 0 < procent_reducere <= 100:
        reducerea = procent_reducere / 100 * pret
        pret_nou = pret - reducerea
        return pret_nou
    else:
        print('Reducerea este invalida!')






