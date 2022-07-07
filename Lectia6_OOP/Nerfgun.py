""""
Exercitiu 'nerfgun'

model
gloante
piedica pusa

constructor - model
descrie()
incarca()
trage()
pune_piedica()
scoate_piedica()

"""


class Nerfgun:
    #atribuute / field uri
    model = None
    culoare = None
    nrgloante = 0
    piedica_pusa = True
    culoriposibile = {'alb', 'negru', 'rosu'}

    #constructor
    def __init__(self, model, culoare):
        self.model = model
        if culoare in self.culoriposibile:  # fortam culoarea sa fie parte din gama disponibila
            self.culoare = culoare
        else:
            print('Culoarea nu este disponibila')

    #metode
    def descrie(self):
        print(f'Modelul este {self.model}')
        print(f'Culoarea este {self.culoare}')
        print(f'Nr de gloante este {self.nrgloante}')
        print(f'Piedica este pusa: {self.piedica_pusa}')

#iitializam obiecte

nerf1 = Nerfgun('ak', 'alb')
nerf1.descrie()
