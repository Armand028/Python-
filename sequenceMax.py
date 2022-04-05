def sequenceMax(s):
    '''liste->int, cette fonction retourne la séquence de chiffre la plus longue'''
    i=0
    a=[]
    k=1
    if len(s)==0:
        return k
    while i<len(s)-1:
        k=1
        if s[i]==s[i+1]:
            k=2
        if len(s)-i>2 and s[i+1]==s[i+2]==s[i]:
            k=3
        if len(s)-i>3 and s[i+2]==s[i+3]==s[i]==s[i+1]:
            k=4
        if len(s)-i>4 and s[i+3]==s[i+4]==s[i]==s[i+1]==s[i+2]:
            k=5
        i+=1
        a.append(k)
    return max(a)
ch=input("Veuillez entrer une liste des valeurs séparées par des espaces").strip().split()
print(sequenceMax(ch))     
