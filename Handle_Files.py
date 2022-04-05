import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file_name=None
    while file_name==None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    return file_name 

def remove_ponctuation(words):
    '''(str)->(str)'''
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in punctuation:
        while(item in words):
            words = words.replace(item, "")
    return words
def is_word(word):
    '''(str)->(str)'''
    wrd=[]
    for i in word:
        if i.isalpha():
            wrd.append(i)
    return wrd
def remove_wordOflen_1(line):
    '''(str)->(str)'''
    wrd=[]
    for i in line:
        if len(i)>=2:
            wrd.append(i)
    return wrd
            

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    dico={}
    result = open(fp.lower()).read().splitlines()
    for i in range(len(result)):
        line=result[i]
        line=remove_ponctuation(line)
        line=line.split(" ")
        line= is_word(line)
        line=remove_wordOflen_1(line)
        for y in range(len(line)):
            line[y]=line[y].lower()
            if line[y] not in dico:
                a=set()
                dico[line[y]]=a
            dico[line[y]].add(i+1)      
    return dico
        
    

    
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    query=query.split(" ")
    #star={}
    if query[0] in D:
        star=D[query[0]]
    for i in range(1,len(query)):
        #if(query[i]) in D:
        star=star&D[query[i]]
    l=[]
    for i in star:
        l.append(i)
    return sorted(l)
    
        
        
        
    
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
a=True
while(a):
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    query=remove_ponctuation(query)
    if query=="q":
        a=False
        continue
    u=query
    u=u.split(" ")
    b=True
    for i in u:
        if i not in d:
            print("Word ",i," not in file")
            b=False
            break
    if b==False:
        continue
    c=find_coexistance(d, query)
    print("The one or more words you entered coexisted in the following lines of the file:\n",c)
    

