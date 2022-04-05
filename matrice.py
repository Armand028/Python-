from  math import sqrt
def modifierMat(matrice):
    ''' matrice->matrice
    Cette fonction retourne une matrice dont les elements paires sont remplacé par leur racine carrrée'''
    j=0
    i=0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]%2==0:
                matrice[i][j]=sqrt(matrice[i][j])
            j+=1
        i+=1
    return matrice
m = int(input("Entrez le nombre de rangees: "))
n = int(input("Entrez le nombre de colonnes: "))
matrice = []
i = 0
while (i < m): 
    j = 0
    matrice.append([])
    while j < n:
        v = int(input("matrice["+str(i)+","+str(j) +"]="))
        matrice[i].append(v)
        j = j + 1
    i = i + 1
print(modifierMat(matrice))
                
