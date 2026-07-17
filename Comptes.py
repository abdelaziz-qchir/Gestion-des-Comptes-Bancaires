class Compte:
    nb = 0
    
    def __init__(self,proprietaire,solde):
        Compte.nb += 1
        self.__numero = Compte.nb
        self.__proprietaire = proprietaire
        self.__solde = solde
    
    @property
    def getNum(self):
        return self.__numero
    
    @property
    def getProp(self):
        return self.__proprietaire
    
    @property
    def getSolde(self):
        return self.__solde
    
    def __str__(self):
        return "Numéro Compte :" + str(self.getNum) + " propriétaire = " + str(self.getProp) + " Solde Initial= " + str(self.getSolde)