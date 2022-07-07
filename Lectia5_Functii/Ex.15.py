# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)

def suma(x):
    item = range(0, x+1)
    for i in item:
        sum = 0
        for j in range(0, i+1):
            sum = sum + j
    print(sum)

suma(3)