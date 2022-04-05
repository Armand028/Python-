def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    for r in range(len(grille)):
        ligne=grille[row]
        if num in ligne:
            return False
        else:
            return True
    # A COMPLETER

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    resul=True
    for r in range(len(grille[0])):
        for j in range(len(grille)):
            colonne=grille[j][col]
            if colonne==num:
                resul=False
                return resul
    return resul
    # A COMPLETER

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    resul=True
    i=row
    while i<=row+2:
        if resul==False:
            return resul
        ligne=grille[i]
        j=col
        while j<=col+2:
            colonne=grille[i][j]
            if colonne==num:
                resul=False
                break
            j+=1
        i+=1
    return resul
            

    # A COMPLETER

def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    resul=True
    for i in range(len(grille)):
        for j in range(len(grille[i])-1):
            left=grille[i][j]
            if grille[i][j]==0:
                resul=False
                return resul
    return resul                
    
   # A COMPLETER
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   valide=False
   ligne=verifierLigne(grille, row, num)
   if ligne==True:
       colonne=verifierCol(grille, col, num)
       if colonne==True:
           sousgrille=verifierSousGrille(grille, row, col, num)
           if sousgrille==True:
               valide=True
               return valide
               
   
   
   # A COMPLETER
   

