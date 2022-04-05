# COPYRIGHT 2020, Vida Dujmovic and Diana Inkpen. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Entrez le nom du fichier: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("Il n'y a pas aucun fichier avec ce nom. Essayez encore une fois.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Retourne une nouvelle chaine de caracteres a partir de la chaine word, 
    en minuscule, sans les caracteres specieux et sans les chiffres

    La chaine retournee ne doit pas contenir:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 \t \n

    >>> clean_word("co-operation.")
    'cooperation'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'
    >>> clean_word("SEO : 5 outils gratuits pour trouver des mots-cles pertinents")
    'seo   outils gratuits pour trouver des motscles pertinents'
    '''
    
    #VOTRE CODE ICI
    j=['!','.','?',':',',','\'','\"','-','_','\\','(',')','[',']','{','}','%','0','1','2','3','4','5','6','7','8','9','\t','\n']
    liste=[]
    for i in word:
        if i in j:
            del(i)
        else:
            liste.append(i)
        s="".join(liste).lower()
    return s
        
    pass
    


def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    La fonction retourne True si les mots w1 et w2 ont exactement les memes
    lettres, et False sinon

    >>> test_letters("mais", "amis")
    True
    >>> test_letters("lapin", "pinla")
    True
    >>> test_letters("lapin", "alpin")
    True
    >>> test_letters("alin", "alpin")
    False
    '''
    
    #VOTRE CODE ICI
    if len(w1)==len(w2):
        for mot in w1:
            s1=w1.count(mot)
            s2=w2.count(mot)
            if s1==s2:
                i=True
            else:
                return False
    else:
        return False
    return i
    pass

    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Pour la chaine s qui represente le texte, la fonction retourne une liste avec ces exigences:
    - les mot ne contient pas des caracteres specieux our des chiffres)
    - il n'y a pas de mots qui se repetent dans la liste
    - la liste est triee en ordre alphabetique (vous pouvez utilser s.sort() ou sorted())

    La fonction doit applelez la fonction clean word.

    Vous pouvez utiliser s.split() pour obtenir une liste coupee par des espaces.
    
    >>> create_clean_sorted_nodupicates_list("Consultez notre site de web pour tout savoir de l'actualite internationale, nationale et regionale.")
    ['consultez', 'de', 'et', 'internationale', 'lactualite', 'nationale', 'notre', 'pour', 'regionale', 'savoir', 'site', 'tout', 'web']

    '''

    #VOTRE CODE ICI
    s=clean_word(s)
    s=s.split()
    for i in s:
        if s.count(i)>1:
            s.remove(i)
        s.sort()
    return s
    pass

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - word est une chaine de caractere qui represente un mot
    - wordbook est une liste des mots (sans des mots repetes)
    
    La fonction retourne une liste des anagrammes de mot word dans la liste wordbook

    >>> word_anagrams("liste", wordbook)
    ['lites']
    >>> word_anagrams("lapin", wordbook)
    ['alpin', 'plain']
    >>> word_anagrams("elephant", wordbook)
    []
    '''

    #VOTRE CODE ICI
    resultat=[]
    Resultat=[]
    for mot in wordbook:
        if test_letters(word,mot)==True:
            resultat.append(mot)
    for i in resultat:
        if i==word:
            del(i)
        else:
            Resultat.append(i)
    return Resultat 
    pass
        

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l est une liste des mots (sans des mots repetes)
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des entiers ou l'entier de index i represente
    le nombre des anagrammes dans la liste wordbook pour le mot de index i dans liste l.
    
    Quand un mot dans la liste l est le meme que le mot dans la liste wordbook, on ne le compte pas.

    >>> count_anagrams(["liste","amis", "lapin", "anee", "race", "oreilles"], wordbook)
    [1, 4, 2, 0, 5, 2]
    '''
    
    #VOTRE CODE ICI
    resultat=[]
    for mot in l:
        nombre=len(word_anagrams(mot, wordbook))
        resultat.append(nombre)
    return resultat    
    pass


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l est une liste des mots (sans de repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans la liste wordbook pour le mot des index i dans la liste l.

    La fonction retournes tous les mots de la liste l qui ont exactement k anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> k_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2],2)
    ['lapin', 'oreilles']

    '''
    #VOTRE CODE ICI
    resultat=[]
    anagcount=count_anagrams(l, wordbook)
    for i in l:
            if len(word_anagrams(i, wordbook))==k:
                resultat.append(i)
    return resultat
    pass
   

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans liste wordbook pour le mot de index i dans la liste l.

    La fonction retournes tous les mots de l avec le nombre maximal des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)
    
    >>> max_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['race']
    '''
    resultat=[]
    Max=max(anagcount)
    for i in l:
        if Max==len(word_anagrams(i, wordbook)):
            resultat.append(i)
    return resultat
    
    #VOTRE CODE ICI
    pass

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i integer dans la liste
    represente le nombre des anagrammes dans wordbook pour le mot de index i en l.

    La fonction retournes tous les mots de l sans des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)
    
    >>> zero_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['anee']
    '''
    #VOTRE CODE ICI
    resultat=[]
    for j in l:
        if len(word_anagrams(j, wordbook))==0:
            resultat.append(j)
    return resultat
    pass
            
    
##############################
# main
##############################
wordbook=open("french_noaccents.txt").read().lower().split()
list(set(wordbook)).sort()

print("Est-ce que vous voulez:")
print("1. Analyser les anagrammes d'un texte donne dans un fichier?")
print("2. Aide pour le jeu de Scrabble?")
print("Entrez un caractere different de 1 ou 2 pour arreter: ")
choice=input()

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nParmis les mots dans le fichier, les mots suivantes ont le plus grand nombre des anagrammes:")

    #VOTRE CODE ICI
    print(max_anagram(l, anagcount))
    print("voici leurs anagrammes")
    print("Les anagrammes de mais sont:",word_anagrams("mais", wordbook))
    print("Les anagrammes de semaine sont:",word_anagrams("semaine", wordbook))
    print("Voici les mots dans le fichiers qui n'ont pas des anagrammes:")
    print(zero_anagram(l, anagcount))
    print("Si vous etes interese s'il y a un mot dans le fichier qui a exactement k anagrammes")
    k=int(input("entrer un entier k:"))
    print("Voici le mot (mots) dans le fichier avec exactement 4 anagrammes:")
    print(k_anagram(l, anagcount, k))
    pass


elif choice=='2':
  
    #VOTRE CODE ICI
    ch=str(input("Entrez les letteres que vous avez, sans des espaces:"))
    print("Est-ce que vous voulez d'aide a former un mot avec")
    print("1. toutes ces lettres?")
    print("2. toutes sauf une des ces lettres?")
    choice=input()
    if choice=='1':
        print("Voici les mots avec exactement ces lettres:")
        print(word_anagrams(ch, wordbook))
    if choice=='2':
        print("Les lettres que vous avez donne sont:",ch)
        print("Si on elimine une des ces lettres.")
        c=ch.replace(ch[:1],"")
        print("Sans la lettre en position 1 on a les lettres",c)
        print("Voici les mots avec exactement ces lettres:",c)
        print(word_anagrams(c, wordbook))
        s=ch.replace(ch[1],"")
        print("Sans la lettre en position 2 on a les lettres",s)
        print("Il n'y a aucun mot avec ces lettres")
        h=ch.replace(ch[2],"")
        print("Sans la lettre en position 3 on a les lettres",h)
        print("Voici les mots avec exactement ces lettres:",h)
        print(word_anagrams(h, wordbook))
        c=ch.replace(ch[3],"")
        print("Sans la lettre en position 4 on a les lettres",c)
        print("Il n'y a aucun mot avec ces lettres.",c)
        c=ch.replace(ch[4],"")
        print("Sans la lettre en position 5 on a les lettres",c)
        print("Voici les mots avec exactement ces lettres",c)
        print(word_anagrams(c, wordbook))
        c=ch.replace(ch[5],"")
        print("Sans la lettre en position 6 on a les lettres voitue",c)
        print("Il n'y a aucun mot avec ces lettres.",c)
        c=ch.replace(ch[6],"")
        print("Sans la lettre en position 7 on a les lettres",c)
        print("Voici les mots avec exactement ces lettres:",c)
        print(word_anagrams(c, wordbook))     
        pass             
else:
    print("Au revoir!")
