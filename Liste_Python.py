def sequenceDesDeux(l):
    '''liste->bool, cette fonction dit s'il y'a ou non une séquence de nombres identique consécutive'''
    i=0
    t=False
    while i<len(l)-1:
        if l[i]==l[i+1]:
            t=True
            if t==True:
                break
        i+=1
    return t
ch=input("Veuillez entrer une liste des valeurs séparées par des espaces:").strip().split()
print(sequenceDesDeux(ch))
