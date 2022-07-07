# functie care sa returneze procentul ramas dintrun rezervor de benzina
# input: cantitate_ramasa, capacitate_rezervor
# daca procentul e sub 15% afisam un warning

def procent_ramas(cantitate_ramasa, capacitate_rezervor):
    if (cantitate_ramasa / capacitate_rezervor)*100 < 15:
        print(str(cantitate_ramasa / capacitate_rezervor*100) + ' %')
        return 'Warning!'
    else:
        return str(cantitate_ramasa / capacitate_rezervor*100) + ' %'


print(procent_ramas(12,100))


