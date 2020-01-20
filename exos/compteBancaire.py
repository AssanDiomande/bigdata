class CompteBancaire :
    def __init__(self) :
        self.nom='Dupont'
        self.solde=100
    
    def depot(self,somme) :
        self.solde = self.solde+somme
    
    def retrait(self,somme) :
        self.solde = self.solde-somme
    
    def affiche(self) :
        print ("Titulaire du compte :{}, solde du compte : {}".format(self.nom,self.solde))
        
compte1 = CompteBancaire()
compte1.retrait(5)
compte1.depot(15)
compte1.affiche()
