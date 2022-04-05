def split_tester(N, d):
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    (str,str)->boolean
    this function tests if an given integer N can be split into pieces that each have d digits
    such that the resulting sequence is strictly increasing
    precondition:N and d are positive integer
    '''
    
    N_length=len(str(N))
    number_Piece=int(N_length/int(d))
    s=""
    index_leap=0
    answer=True
    a=int(d)
    if N_length==int(d):
        s=N
    else:
        if(d=='1'):
            for i in range(number_Piece):
                substrings=N[index_leap]
                index_leap=index_leap+1
                if i==0:
                    s=substrings
                else:
                    s=s+", "+substrings
        else:
            for i in range(0,number_Piece):   
                substrings=N[index_leap:a]
                index_leap=index_leap+int(d)
                a=a+int(d)
                if i==0:
                    s=substrings
                else:
                    s=s+", "+substrings
    x=0
    h=int(d)
    for i in range(number_Piece-1):
        subs0=N[x:h]
        subs1=N[x+int(d):h+int(d)]
        if int(subs0)>int(subs1):
            answer=False
            break
        x=x+int(d)
        h=h+int(d)
    print(answer)
    if(answer==True):
        print(s)
        print("The sequence is increasing")
    else:
        print(s)
        print("The sequence is not increasing")
    return s
# you can add more function definitions here if you like
#######################################################################
def ascii_name_plaque(name):
    '''
    (string)->()
    draws a name plaque with the given name
    '''
    print("***"+"*"*(len(name)+4)+"***")
    print("*"+" "*(len(name)+8)+"*")
    print("*"+"  "+"__"+name+"__"+"  *")
    print("*"+" "*(len(name)+8)+"*")
    print("***"+"*"*(len(name)+4)+"***")
#######################################################################
            
               


            
# main
# Your code for the welcome message goes here, instead of name="Vida"
ascii_name_plaque("Welcome to my increasing-splits tester")
name=(input("What is your name?  ")).strip()
s=name+", "+"welcome to my increasing-splits tester."
ascii_name_plaque(s)
flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    #YOUR CODE GOES HERE. The next line should be elif or else.
    elif question!="yes":
        print("Please enter yes or no. Try again.")
    else:
        print("Good choice!")
        value=input("Enter a positive integer: ")
        value=value.strip()
        if(value.isdigit()==True):
            if not int(value)>0:
                print("The input has to be a positive integer.Try again.")
            else:
                split=input("Input the split. The split has to divide the length of "+str(value)+" i.e "+str(len(str(value)))+" ")
                split=split.strip()
                if(split.isdigit()==True):
                    if(len(str(value))%int(split)!=0):
                        print(split, "does not divide ",len(str(value)),". Try again.")
                    else:
                        split_tester(value,split)
                else:
                    print("The split can only contain digits. Try again")
        else:
            print("The input can only contain digits. Try again.")
        
#finally your code goes here too.
s="Good buy "+name+"!"
if(flag==False):
    ascii_name_plaque(s)
    
