import datetime


class Factura:
    seria = 'ABC'
    numar = 0
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def sch_cantitatea(self,cantitate_noua):
        self.cantitate = cantitate_noua

    def sch_pretul(self,pret_nou):
        self.pret_buc = pret_nou

    def sch_nume(self, nume_nou):
        self.nume_produs = nume_nou

    def genereaza_factura(self):
        total = self.cantitate * self.pret_buc
        factura = [self.nume_produs, self.cantitate,self.pret_buc,total]
        from datetime import date
        azi = date.today()
        print (f'Factura seria {self.seria} numar {self.numar}')
        print(f'Data este: {azi}')
        print("{:<15} {:<20} {:<10} {:<15}".format('Nume', 'Cantitate', 'Pret', 'Total'))
        print("{:<15} {:<20} {:<10} {:<15}".format(self.nume_produs, self.cantitate, self.pret_buc, total))



factura1 = Factura(1,'telefon',5,1)
factura1.genereaza_factura()
factura1.sch_nume('inghetata')
factura1.sch_pretul(100)
factura1.sch_cantitatea(20)
factura1.genereaza_factura()