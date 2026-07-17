from Comptes import Compte

class CompteCourant(Compte):
    def __init__(self, proprietaire, solde, montantDecouvert):
        super().__init__(proprietaire, solde)
        self.__montantDecouvert=montantDecouvert
        print(f"Compte.nb: {Compte.nb}")
    
    @property
    def getMontantDecouvert(self):
        return self.__montantDecouvert
    
    def __str__(self):
        return Compte.__str__(self) + "Montant découvert " + self.getMontantDecouvert