# 3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat():
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele angajatului este {self.nume}')
        print(f'Prenumele angajatului este {self.prenume}')
        print(f'Salariul angajatului este {self.salariu}')

    def nume_complet(self):
        print(f'Numele complet este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul anual este {salariu_anual}')

    def marire_salariu(self, procent):
        marire_salariu = self.salariu * procent / 100
        self.salariu = self.salariu + marire_salariu
        print(f'Marirea lunara primita de angajat va fi: {marire_salariu}, insemnand {procent}%. Noul salariu este: {self.salariu}')


angajat1 = Angajat('Andra', 'Trifu', 1600)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)

angajat2 = Angajat('Lola', 'Mathers', 2639)
angajat2.descrie()
angajat2.nume_complet()
angajat2.salariu_anual()
angajat2.salariu_lunar()
angajat2.marire_salariu(5)
angajat2.salariu_lunar()
angajat2.descrie()

#  salariul anual nu ia in calcul majorarea aplicata prin marire_salariu (cel lunar, da)

