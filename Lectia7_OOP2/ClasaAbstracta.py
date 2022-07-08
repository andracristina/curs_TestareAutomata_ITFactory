from abc import abstractmethod

pi = 3.14

class FormaGeometrica:


    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):     # de revizuit - Implementati getter, setter, deleter pt latura
    __latura = None # latura este proprietate privata

    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        a = self.latura**2
        return a

class Cerc(FormaGeometrica):    # mplementati getter, setter, deleter pt raza
    __raza = None
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        a = pi * self.__raza**2
        return a

    def descrie(self):
        print('Eu nu am colturi!')

patrat1 = Patrat(3)
print(patrat1.aria())


cerc1 = Cerc(32)
print(cerc1.aria())
cerc1.descrie()


