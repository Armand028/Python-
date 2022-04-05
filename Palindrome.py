def triangle(n):
    ''' int->str, retourne un triangle fait d'étoiles
    '''
    if n==1:
        s="*"
    else:
        s="*"*(n)
        triangle(n-1)
    print(s)
####################################################################################
def prodListePos_rec(l,n):
    ''' (list,int)->float, retourne le produit des éléments positifs de la liste'''
    p=1
    n>=0
    if l[n-1]>0:
        k=l[n-1]
    else:
        k=1
    p=p*k
    if n==0:
        if l[0]>0:
            k=l[0]
        else:
            k=1
        return p*k
    c=prodListePos_rec(l,n-1)
    return p*c

######################################################################################
def palindrome(ch):
    ''' str->bool, retourne une booleenne si un mot est palindrome ou pas c'est a dir si le mot est égale à son inverse'''
    if len(ch)==1 or len(ch)==0:
        return True
    else:
        if ch[0]==ch[len(ch)-1]:
            result=True
            c=palindrome(ch[1:(len(ch)-1)])
            return result and c
        else:
            return False
