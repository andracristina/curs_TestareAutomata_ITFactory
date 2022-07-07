class Cont:
    iban = None
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul are in cont suma de {self.sold} RON')

    def debitare_cont(self,suma):
        sold_nou = self.sold - suma
        self.sold = sold_nou
        print(f'Contul a fost debitat cu {suma} RON. Noul sold este {sold_nou}')

    def creditare_cont(self,suma):
        sold_nou = self.sold + suma
        self.sold = sold_nou
        print(f'Contul  a fost debitat cu {suma} RON. Noul sold este {sold_nou}')


cont1 = Cont(1,'ion',10)
cont1.afisare_sold()
cont1.debitare_cont(10)
cont1.creditare_cont(10)

cont2 = Cont(2,'andra',25)
cont2.afisare_sold()
cont2.creditare_cont(100)
cont2.debitare_cont(25)