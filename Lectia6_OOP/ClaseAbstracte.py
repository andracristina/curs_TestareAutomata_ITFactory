from abc import ABC, abstractmethod # e nevoie de acest import pt abstractizare

class Car(ABC): # Car mosteneste atributele ABC / car initialises ABC
    @abstractmethod # este un decorator ca sa evidentiem mai bine faptul ca e o metoda abstracta
    def accelerate(self):
        pass
        # sau raise NotImplementedError

    @classmethod # decorator pt class method
    def stop(self):
        print('Stop!')

# o metoda abstracta este o metoda care nu contine nici o logica
