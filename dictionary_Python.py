def calculPrix(article, quantite):
    ''' str->float cette fonction permet de calculer le prix total d'un article'''
    return (p[article])*quantite
def calculTotal(article1, quantite1, article2, quantite2, article3, quantite3):
    '''(str,int,str,int,str,int)->float, cette fonction calcule le prix total des articles'''
    return calculPrix(article1, quantite1)+calculPrix(article2, quantite2)+calculPrix(article3, quantite3)
def validerCommande(article1, quantite1, article2, quantite2, article3, quantite3):
    '''(str,int,str,int,str,int)->bool, cette fonction permet de comfirmer que les éléments choisis
        sont disponibles'''
    resultat=False
    if article1 in p and article2 in p and article3 in p and quantite1<=(q[article1]) and quantite2<=(q[article2]) and quantite3<=(q[article3]):
        resultat=True
    return resultat
q = {"bureau":9, "chaise":25, "imprimante":46, "scanneur":17}
p = {"bureau":75.9, "chaise":50.9, "imprimante":32.5, "scanneur":28.0}
article1=str(input("Entrer le premier article:"))
quantite1=int(input("Entrer la quantité de votre 1er article:"))
article2=str(input("Entrer le deuxième article:"))
quantite2=int(input("Entrer la quantité de votre 2eme article:"))
article3=str(input("Entrer le troisième article:"))
quantite3=int(input("Entrer la quantité de votre 3eme article:"))
valide=validerCommande(article1, quantite1, article2, quantite2, article3, quantite3)
if valide==True:
    prix=calculTotal(article1, quantite1, article2, quantite2, article3, quantite3)
    print("Le prix total de votre commande est:",prix,".$","Merci et à la prochaine")
    q[article1]=q[article1]-quantite1
    q[article2]=q[article2]-quantite2
    q[article3]=q[article3]-quantite3
    print("Les quantités disponibles après l'achat sont:",q)
else:
    print("Votre commande est annulée.SVP,vérifier les articles ou les quantités.")
    print()
    print("Les quantités disponibles après l'achat sont:\n",q)
    
    
    
    
                       

        
        


