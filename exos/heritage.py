class DateNaissance:
    jour=0
    mois=0
    année=0
    
    def __init__(self,jour,mois,annee) :
        self.jour = jour
        self.mois = mois
        self.annee = annee
        
    def toString(self) :
        print("Date de naissance : %2d/%2d/%d"%(self.jour,self.mois,self.annee))
        

class Personne(DateNaissance):
    nom=""
    prenom=""
    dateDeNaissance=""
    
    def __init__(self,nom,prenom,DateNaissance) :
        self.nom=nom
        self.prenom=prenom
        self.dateDeNaissance=DateNaissance
    
    def afficher(self) :
        print("Nom : %s , Prenom %s "%(self.nom,self.prenom))
        self.dateDeNaissance.toString()
        
class Employe(Personne):
    personne=Personne
    salaire=""
    
    def __init__(self,personne,salaire):
        self.personne=
        