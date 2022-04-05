# Family name: Armand Guigma 
# Student number:
# Course: IT1 1120 
# Assignment Number 2
# year 2021


import math
import random


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    (number,number)->(number)
    this fonction helps elementary student practice exponentional and its inverse operation 
    '''
    if flag==0:
        if n==2:
            correct_Ans=0
            generated_Number=random.randint(1,10)
            print("Question 1")
            response1=int(input("2 to what is "+str(2**generated_Number)+ " i.e. what is the result of log_2("+str(2**generated_Number)+")"))
            if response1==generated_Number:
                correct_Ans=correct_Ans+1
            print("Question 2")
            generated_Number=random.randint(1,10)
            response2=int(input("2 to what is "+str(2**generated_Number)+ " i.e. what is the result of log_2("+str(2**generated_Number)+")"))
            if response1==generated_Number:
                correct_Ans=correct_Ans+1
        elif n==1:
            correct_Ans=0
            generated_Number=random.randint(1,10)
            print("Question 1")
            response3=int(input("2 to what is "+str(2**generated_Number)+ " i.e. what is the result of log_2("+str(2**generated_Number)+")"))
            if repsonse3==generated_Number:
                correct_Ans=correct_Ans+1
        else :
            correct_Ans=0
            print("Zero questions. OK. Good bye")
    elif flag==1:
        correct_Ans=0
        if n==2:
            generated_Number=random.randint(1,10)
            print("Question 1:")
            response4=int(input("What is the result of 2^"+str(generated_Number)+"?"))
            if response4==2**generated_Number:
                correct_Ans=correct_Ans+1
            print("Question 2:")
            generated_Number=random.randint(1,10)
            response5=int(input("What is the result of 2^"+str(generated_Number)+"?"))
            if repsonse5==2**generated_Number:
                correct_Ans=correct_Ans+1
        elif n==1:
            generated_Number=random.randint(1,10)
            print("Question 1:")
            response6=int(input("What is the result of 2^"+str(generated_Number)+"?"))
            if response6==2**generated_Number:
                correct_Ans=correct_Ans+1
        elif n==0:
            print("Zero questions. OK. Good bye")
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
    else:
        print(" Invalid choice. Only 0 or 1 is accepted")
    return correct_Ans
#####################################################################################
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
##############################################################################################
def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    (number,number,number)->()
    this fonction resolve a quadratic equation with given coefficients a,b,c
    '''
    if(a!=0 and b!=0 and c!=0):
        if(b**2-4*a*c)>=0:
            print("The quadratic equation", a,"*x^2", "+", b,"*x" ,"+ ", c," ="," 0 ", "has the following two real roots: ")
            print((-b-math.sqrt(b**2-4*a*c))/2*a)
            print("and")
            print((-b+math.sqrt(b**2-4*a*c))/2*a)
        else:
            print("The quadratic equation", a,"*x^2", "+", b,"*x" ,"+ ", c," ="," 0 ", "has the following two complex roots: ")
            print(-b/2*a,"-","i ",math.sqrt(-(b**2-4*a*c))/2*a)
            print("and")
            print(-b/2*a,"+","i ",math.sqrt(-(b**2-4*a*c))/2*a)
    elif(a==0 and b!=0 and c!=0):
        print("The linear equation", b,"*x" ,"+ ", c," ="," 0 ", "has the following root: ")
        print(-c/b)
    elif(a==0 and b==0 and c!=0):
        print("the quadratic equation",c," ="," 0 ")
        print("is satisfied for no number x")
    else:
        print("The quadratic equation", a,"*x^2", "+", b,"*x" ,"+ ", c," ="," 0 ")
        print("is satisfied for all numbers x")
        
           



# main

# your code for the welcome tmessage goes here
ascii_name_plaque("Welcome to my math quiz-generator")
name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    ascii_name_plaque(name+", welcome to my quiz-generator for elementary school students")
    opera_choice=int(input("what do you want to practice, enter \n0 to practice the inverse of exponentiation or \n1 to practice  the exponentiation\n"))
    if (opera_choice!=0 and opera_choice!=1):
        print("Only 0or 1 are valid choices .")
    number_question=int(input(" How many questions would you like for your practice\n"))
    if (number_question!=0 and number_question!=1 and number_question!=2):
        print("Only 0,1, or 2 are valid choices for the number of questions.")
    number= elementary_school_quiz(opera_choice,number_question)
    if number==2:
        print("Congratulations ",name,"  You’ll probably get an A tomorrow.")
    if number==1:
        print("You did ok ",name,"  but I know you can do better.")
    if number==0:
        print("I think you need some more practice ",name)
elif status=='2':

    # your code for welcome message
    ascii_name_plaque("quadratic equation, a·x^2 + b·x + c= 0, solver for "+name)
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question=question.lower()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a=float(input("Enter a number the coefficient a: "))
            b=float(input("Enter a number the coefficient b: "))
            c=float(input("Enter a number the coefficient c: "))
            high_school_quiz(a,b,c)
 
else:
    # your code goes here
    print(name," you are not a target audience for this software.")

print("Good bye "+name+"!")
