class Car:
    #fields/atribute
    marca = 'Dacia' # la momentul initializarii, obiectele de tip Car vor fi Dacia; se poate suprascrie
    culoare = None # sau 'gri' - alta metoda ar fi sa ii dam aici o culoare si apoi sa construim o metoda de 'vopsire'
    model = None

    #constructor
    def __init__(self, culoare, model):
        #self.culoare = culoare   # self reprezinta un placeholder pt viitorul obiect (nu ii stim numele, ex. car1 )
        if culoare == 'orange':   # pot scrie orice bucata de cod aici; e posibil sa modificam ceea ce vine din input
            self.culoare = 'portocaliu'
        self.model = model







#############################################################
car1 = Car('alb', 'Logan')  #aici includem parametri / atributele cerute in constructor; fara ele, eroare lipsa parametri
car1.culoare = 'orange' # aici se suprascrie daca mai sus este o culoare 'default'
print(car1.model)
print(car1.culoare)