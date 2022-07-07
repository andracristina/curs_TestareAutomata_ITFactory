# 2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = 0

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea este {self.lungime}')
        print(f'Latimea este {self.latime}')
        print(f'Culoare este {self.culoare}')

    def aria(self):
        aria = self.latime * self.lungime
        print(f'Aria este {aria}')

    def perimetru(self):
        perimetru = 2*self.latime + 2*self.latime
        print(f'Petrimetrul este {perimetru}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

dreptunghi1 = Dreptunghi(2,3, 'gri')
dreptunghi2 = Dreptunghi(3,4, 'alb')

dreptunghi2.descrie()
dreptunghi2.aria()
dreptunghi2.perimetru()
print()
dreptunghi1.descrie()
dreptunghi1.aria()
dreptunghi1.perimetru()
dreptunghi1.schimba_culoarea('roz')
dreptunghi1.descrie()
