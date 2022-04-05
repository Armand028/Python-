def nombreDivisibles(l,n):
    ''' (liste, int)->int  cette fonction returne le nombre de diviseurs de n contenu dans la liste l'''
    j=0
    for i in l:
        if int(i)%n==0:
            j+=1
    return j
ch=input("entrer des nombres sépareés par des espaces:").strip().split()
Nombre=int(input("entrer un nombre:"))
print("le nombre des éléments divisible par",Nombre,"est",nombreDivisibles(ch,Nombre))
