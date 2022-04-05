class Personne:
    '''represente une classe Personne'''
    def __init__(self, nom, prenom, identifiant):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        self.nom=nom
        self.prenom=prenom
        self.identifiant=identifiant

    def __repr__(self):
        '''(Personne)->str
        retourne une representation de l'objet'''
        # A completer
        return "nom: "+ str(self.nom)+"pronom: "+str(self.prenom)+"identifiant: "+str(self.identifiant)

    def __eq__(self, autre):
        '''(Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes'''
        # A completer
        return self.nom==autre.nom and self.prenom==autre.prenom and self.identifiant==autre.identifiant

class Etudiant(Personne):
    '''represente une classe Etudiant'''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)
     
     # methodes
    def __init__(self, nom, prenom, identifiant,solde,cours=[]):
        '''(str,str, int,float,list)->None
        initialise les attributs de la classe Etudiant'''
        Personne.__init__(self,nom, prenom, identifiant)
        self.solde=solde
        self.cours=cours
    def __repr__(self):
        '''(Etudiant)->str
        retourne une representation de l'objet'''
        return "nom: "+ str(self.nom)+" pronom: "+str(self.prenom)+" identifiant: "+str(self.identifiant)+" solde "+str(self.solde)+" cours "+str(self.cours)
    def ajouterCours(self,cours):
        '''list->list  retourne une liste de cours'''
        if self.solde==0:
            self.cours.append(cours)
            return True
        else:
            return False
     # A completer
    

class Employe(Personne):
    '''represente un employe'''
    # tauxHoraire est un attribut de la classe Employe
    # methodes
    def __init__(self,nom,prenom,identifiant,tauxHoraire):
        '''(str,str, int,float)->None
        initialise les attributs de la classe Etudiant'''
        Personne.__init__(self,nom, prenom, identifiant)
        self.tauxHoraire=tauxHoraire
    def __repr__(self):
        '''(Employe)->str
        retourne une representation de l'objet'''
        return " nom:"+ str(self.nom)+" prenom: "+str(self.prenom)+" identifiant: "+str(self.identifiant)+" taux Horaire "+str(self.tauxHoraire)
    def calculerSalaire(self,heure):
        '''int->float, retourne le salaire'''
        return heure*self.tauxHoraire

        

    # A completer

class Gestion:
 listEtudiant = []
 listEmploye = []
 def ajouterEtudiant(self):
    ''' none -> bool
    ajouter un etudiant dans une liste d'etudiants'''
    # A completer
    nom=str(input("enter le nom:"))
    prenom=str(input("entrer le prenom:"))
    identifiant=int(input("entrer identifiant:"))
    solde=float(input("entrer le solde:"))
    cours=input("entrer une liste de cours:").split()
    etu=Etudiant(nom, prenom, identifiant,solde,cours)
    s=input("voulez-vous ajouter un autre cours?")
    if s=="oui":
        c=input("ajouter un autre cours:")
        if etu.solde==0:
            etu.cours.append(c)
        else:
            print("veuiller payer votre solde avant d'ajouter un cours")
    elif s=="non":
        print("Vouz avez choisi de ne pas ajouter aucun cours.")
    else:
        print("entrer oui ou non svp")
    if etu not in Gestion.listEtudiant:
        Gestion.listEtudiant.append(etu)
        print("Etudiant ajoute avec succes.")
        return True
    else:
        print("etudiant existe déjà")
        return False

 def ajouterEmploye(self):
    ''' none -> bool
    ajouter un employe dans une liste d'employes'''
    # A completer
    nom=str(input("entrer le nom:"))
    prenom=str(input("entrer le prenom:"))
    identifiant=int(input("entrer identifiant:"))
    tauxHoraire=float(input("entrer taux horaire:"))
    employ=Employe(nom,prenom,identifiant,tauxHoraire)
    if employ not in Gestion.listEmploye:
        Gestion.listEmploye.append(employ)
        print("Employe ajoute avec succes.")
    else:
        print("ce employer existe déjà")
    
    
 def SoldeNonPaye(self):
    ''' none -> float
    retourner le nombre des etudiants qui ont un solde non paye'''
    # A completer
    l=0
    for etu in Gestion.listEtudiant:
        if etu.solde!=0:
            l+=1
    return l

 def salaireInd(self, employe, heures):
    '''(str) -> float
    retourne le salaire d'un employe'''
    # A completer
    s=0
    if employe in Gestion.listEmploye:
        s=heures*employe.tauxHoraire
        return s
    else:
        return s
    


#program principal
g = Gestion()
print("Ajoutez des etudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajouter des employes.")
g.ajouterEmploye()
g.ajouterEmploye()

# Afficher le nombre des employes et des etudiants
print("il y a: ", len(Gestion.listEtudiant), " etudiants.")
print("il y a: ", len(Gestion.listEmploye), " employes.")
# Afficher le nombre des etudiants qui ont un solde a payer
print("il y a ", g.SoldeNonPaye(), "etudiants qui n'ont pas paye leur solde.")
# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    heure = int(input("Entrez le nombre des heures pour employe " + e.prenom + " " + e.nom + " "))
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e, heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)
