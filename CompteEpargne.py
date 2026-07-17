from Comptes import Compte

class CompteEpargne(Compte):
    def __init__(self,proprietaire,solde,interet):
        super().__init__(proprietaire, solde)
        self.__interet=interet
        print(f"Compte.nb: {Compte.nb}")
    
    @property
    def getInteret(self):
        return self.__interet
    
    @property
    def getInteret(self):
        return self.__interet
    
    def __str__(self):
        return Compte.__str__(self) + "Interet " + self.getInteret