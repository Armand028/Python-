# Family name: Armand Guigma 
# Student number:
# Course: IT1 1120 
# Assignment Number 2
# year 2021



##################################################################
# Question 1
###################################################################

def min_enclosing_rectangle(radius,x,y):
    '''
    (float,float,float)->(tuple)
    Returns the coordinates of the bottom-left corner of the rectangle enclosing the circle of a given radius
    '''
    if(radius<0):
        return
    else:
        xs=x-radius
        ys=y-radius
        return xs,ys


##################################################################
# Question 2
###################################################################
def vote_percentage(results):
     '''(str)-> float
     Precondition: results have at least one yes and one no
     Returs the percentage of yes
     '''
     yes=results.count('yes')
     no=results.count('no')
     total=yes+no
     return yes/total

##################################################################
# Question 3
###################################################################
def vote():
    '''()-> str
     Returs the result of a vote
    '''
    results=input("Enter the yes, no, abstained votes one by one and then press enter: ")
    yes_percentage=vote_percentage(results)
    if yes_percentage==1.00:
        print("proposal passes unanimously")
    elif yes_percentage>=2/3:
        print("proposal passes with super majority")
    elif yes_percentage>=1/2:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
###################################################################
# Question 4
###################################################################
def l2lo(w):
    '''
    (float)-> tuple
    Precondition: w is a non-negative number
    returns a pair of numbers
    '''
    l=int(w)
    o=16*(w-l)
    if o>=16:
        x=int(o//16)
        l=l+x
        o=16*(o-16*x)
    return l,o
        
    
    
