# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

import math
from math import pi


class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie(self):
        print(f'Raza cercului este {self.raza}')
        print(f'Culoarea cercului este {self.culoare}')

    def aria(self):
        aria = pi * (self.raza**2)
        print(f'Aria este {aria}')
    def diametru(self):
        diametru = 2 + self.raza
        print(f'Diametrul este {diametru}')
    def circumferinta(self):
        circumferinta = 2 * pi * self.raza
        print(f'Circumferinta este {circumferinta}')


cerc1 = Cerc(1, 'roz')
cerc1.descrie()
cerc1.aria()
cerc1.diametru()
cerc1.circumferinta()

print()

cerc2 = Cerc(5, 'alb')
cerc2.descrie()
cerc2.aria()
cerc2.diametru()
cerc2.circumferinta()