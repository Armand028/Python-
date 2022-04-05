def vote_pourcentage(String):
    '''cette fonction donne le resultat d'un vote
         (str)-> float
         la fonction prend comme valeur les mots oui non et abstention'''
    Num_oui=String.count(Str1)
    Num_non=String.count(Str2)
    Resultat=(Num_oui*100)/(Num_oui+Num_non)
    return Resultat
String=str(input("Entrer les votes séparés par des espaces:"))
Str1="oui"
Str2="non"
Num_oui=String.count(Str1)
Num_non=String.count(Str2)
vote_pourcentage(String)
Resultat=(Num_oui*100)/(Num_oui+Num_non)
if (Resultat==100):
    print("unanimité")
elif(Resultat>=66.67 and Resultat<100):
    print("majorité claire")
elif(Resultat>=50 and Resultat<66.67):
    print("majorité simple")
else:
    print("la motion ne passe pas")
        
