import random
def effectuezTest(opération):
    '''int-> int
       la fonction permet de faire des exercices de soustractions ou exponentielles
       opération= 1 ou 0 d'autres valeurs ne sont pas acceptées'''
    i=0
    j=0
    if(opération==0):
        print("SVP donnez les reponses aux soustractions suivantes:")
        for j in range(0,10):
             n1 = random.randint(0,9)
             n2 = random.randint(0,9)
             resultat=n1-n2
             reponse=int(input(str(n1)+"-"+str(n2)+"="))
             if(resultat==reponse):
                i=i+1
             else:
                print("incorrect-la reponse est:",resultat)
        j=j+1
        print(i,"bonnes reponses")
        if(i<=6):
            print("Demandez à votre enseignant(e) de vous aider")
        else:
            print("Félicitation")
        return i
            
    elif(opération==1):
        print("SVP donnez les reponses aux exponetiations suivantes:")
        for j in range(0,10):
             n1 = random.randint(0,9)
             n2 = random.randint(0,9)
             resultat=n1**n2
             reponse=int(input(str(n1)+"**"+str(n2)+"="))
             if(resultat==reponse):
                 i=i+1
             else:
                 print("incorrect-la reponse est:",resultat)
        j=j+1
        print(i,"bonnes reponses")
        if(i<=6):
            print("Demandez à votre enseignant(e) de vous aider")
        else:
            print("Félicitation")
    else:
        return -1
print("Ce logiciel va effectuez un test avec 10 questions.")
choix=int(input("SVP choisisser l'operation 0) soustraction 1) exponentiation (0 ou 1):"))
effectuezTest(choix)

