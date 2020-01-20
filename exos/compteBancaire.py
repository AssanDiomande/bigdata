class CompteBancaire :
        
    def __init__(self,nom='Dupont',solde=100) :
            self.nom=nom
            self.solde=solde
    
    def depot(self,somme) :
        self.solde = self.solde+somme
    
    def retrait(self,somme) :
        self.solde = self.solde-somme
    
    def affiche(self) :
        print ("Titulaire du compte :{}, solde du compte : {}".format(self.nom,self.solde))
        
compte1 = CompteBancaire('Assan',100)
compte1.retrait(0)
compte1.affiche()
