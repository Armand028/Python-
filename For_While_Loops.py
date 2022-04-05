#Exercice1
def somme_diviseurs_impaires(n):
    '''int->int ,cette fonction retourne la somme des diviseurs impaires'''
    i=1
    Somme=0
    if(n==0):
        return
    else:
        while(i<=abs(n)):
            a=n%i
            b=i%2
            if (a==0 and b==1):
                Somme=Somme+i
            i+=1
        return Somme

    
#Exercice2

def somme_de_serie():
    '''int->float cette fonction calcule une série d'un nombre positif ou nul'''
    somme=1000
    i=1
    a=int(input("entrer un entier positif:"))
    if a<0:
        return
    elif(a==0):
        return somme
    else:
        while(i<=a):
            n=i*i
            somme=somme+1/n
            i+=1
        return somme
#Exercice3
def somme_liste_div2(l):
    '''list->int  cette fonction calcule la moitier des éléments pairs d'une liste'''
    somme=0
    for i in l:
        if(i%2==0):
            somme=somme+i
    return somme
#Exercice4

def  countMembers(s):
    '''list->int  cette fonction donne le nombre de caractère extraordinaires contenu dans une chaine
         les caractères extraordinaires étant ceux contenu dans le liste ci dessous'''
    l=['e','f','g','h','i','j','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','2','3','4','5','6','!',',','\\']
    somme=0
    i=0
    j=0
    k=0
    while i<len(s):
        a=0
        j=str(s[i])
        for a in range (0,len(l)):
            k=str(l[a])
            if(j==k):
                somme=somme+1
        i+=1
    return somme
#Exerci5

def nombre(s):
    '''int->int cette fonction renvoie un nombre sans donné sans les espaces. si le nomùbre saisi contre autre chose que des espaces et des chiffre la fonction return rien'''
    i=[]
    v=""
    for j in s:
        if (j==" "):
            del(j)
        elif(j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9' or j=='-'):
            i.append(j)
        else:
            return None
    for x in i:
        v=v+str(x)
    return v

#Exercice 6

def alienNumbers(s):
    ''' str->int cette fonction permet de traduire un message en un nombre elle ne prende que des chaine de caractère en entrée'''
    somme=0
    for i in s:
        somme=s.count('T')*1024+s.count('y')*598+s.count("!")*121+s.count('a')*42+s.count('N')*6+s.count('U')*1
    return somme

#Exercice 7
def  alienNumbers2(s):
    '''str->int, cette fonction traduit un message donné en caractères en nombre'''
    number_T=0
    number_y=0
    number=0 # number of !
    number_a=0
    number_N=0
    number_U=0
    somme=0
    for i in s:
        if(i=='T'):
            number_T+=1
        elif(i=='y'):
            number_y+=1
        elif(i=='!'):
            number+=1
        elif(i=='a'):
            number_a+=1
        elif(i=='N'):
            number_N+=1
        elif(i=='U'):
            number_U+=1
        somme=number_T*1024+number_y*598+number*121+number_a*42+number_N*6+number_U*1
    return somme

#Exercice 8
def encrypt(s):
    ''' str->str, la foction sert à crypter un message'''
    j=[]
    j.append(s[len(s)-1])
    j.append(s[0])
    i=2
    while (len(s)%2==0 and i<=len(s)/2):
        j.append(s[len(s)-i])
        j.append(s[i-1])
        i+=1
    while (len(s)%2==1 and i<=(len(s)//2)+1):
        if(len(s)%2==1 and i<(len(s)//2)+1):
            j.append(s[len(s)-i])
            j.append(s[i-1])
        if i==(len(s)//2)+1:
            j.append(s[len(s)-i])
        i+=1   
    return "".join(j) 
    



#Exercice 9

def  weaveop(s):
    '''str->str cette fonction retoure une chaine de caractère en ajouant des lettre'''
    j=[]
    i=0
    while i<len(s)-1:
        if (s[i].isalpha() and s[i+1].isalpha()):
            if s[i].islower():
                j.append(s[i])
                j.append("o")
            if s[i+1].islower():
                j.append("p")
        if s[i].isupper():
            j[i+1]="O"
        elif s[i+1].isupper():
            j[i+2]="P"
        elif ((s[i].isalpha() and s[i+1].isdigit()) or (s[i].isdigit() and s[i+1].isalpha())):
            j.append(s[i])
            j.append(s[i+1])
        elif(s[i].isdigit() and s[i+1].isdigit()):
            j.append(s[i])
            j.append(s[i+1])
            
        i+=1
    if i==len(s)-2:
        j.append(s[i+1])
    if i==len(s)-1 and s[i].isalpha():
        j.append(s[i])
    if(len(s)==1 or len(s)==0):
                     return s
    resultat="".join(j)
    return resultat

#Exercice 10
def squarefree(s):
    '''str->bool, cette fonction montre si une expression est squarefree ou pas c'est à dire si deux caractères consécutif du mot sont identiques'''
    i=0
    r=True
    if len(s)==0 or len(s)==1:
        return r
    while i<len(s)/2+1:
        s1=s[i]
        s2=s[i+1]
        if (s1==s2):
            r=False
            return r
        if (r==True and i+2<len(s)):
            s1=s[i]+s[i+1]
            s2=s[i+1]+s[i+2]
            if(s1==s2):
                r=False
                return r
            if(r==True and i+5<len(s)):
                s1=s[i]+s[i+1]+s[i+2]
                s2=s[i+3]+s[i+4]+s[i+5]
                if(s1==s2):
                    r=False
                    return r
                if(r==True and i+7<len(s)):
                    s1=s[i]+s[i+1]+s[i+2]+s[i+3]
                    s2=s[i+4]+s[i+5]+s[i+6]+s[i+7]
                    if(s1==s2):
                        r=False
                        return r
        i+=1
    return r
    
        
        
    
    














