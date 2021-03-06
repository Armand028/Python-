# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     for i in range(0,len(deck)-1,2):
         other.append(deck[i])
         dealer.append(deck[i+1])
     return (dealer, other)
 
def count_num(c,l):
    '''
    (str,list)->(int)
    this function return the number of time the rank of a card appear in the list l
    '''
    count=0
    if len(c)==2:
        for i in l:
            if len(i)==len(c) and i[0]==c[0]:
                count+=1
    elif len(c)==3:
        for i in l:
            if len(i)==len(c) and i[0]==c[0] and i[1]==c[1]:
                count+=1
    return count
            
def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9???', '5???', 'K???', 'A???', 'K???', 'K???', '2???', 'Q???', 'K???', 'Q???', 'J???', 'A???', '4???', '5???', '7???', 'A???', '10???', 'Q???', '8???', '9???', '10???', 'J???', '10???', 'J???', '3???'])
     ['10???', '2???', '3???', '4???', '7???', '8???', 'A???', 'J???', 'Q???']
     >>> remove_pairs(['10???', '2???', '5???', '6???', '9???', 'A???', '10???'])
     ['2???', '5???', '6???', '9???', 'A???']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE       
    for i in range(len(l)):
        if l[i]!=" ":
            a=count_num(l[i],l)
            if a==2 or a==4 or a==3:
                for j in range(len(l)):
                    if l[j]!=l[i]:
                        if len(l[i])==2==len(l[j]):
                            if a==2 or a==4:
                                if l[i][0]==l[j][0]:
                                    l[j]=" "
                                    l[i]=" "
                            elif a==3:
                                if l[i][0]==l[j][0]:
                                    l[j]=" "
                        elif len(l[i])==len(l[j])==3:
                            if a==2 or a==4:
                                if l[i][0]==l[j][0] and l[i][1]==l[j][1]:
                                    l[i]=" "
                                    l[j]=" "
                            elif a==3:
                                if l[i][0]==l[j][0] and l[i][1]==l[j][1]:
                                    l[j]=" "
    while " " in l:
        l.remove(" ")
    no_pairs=l
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    s=""
    for i in deck:
        s=s+i+" "
    print(s)
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     a=True
     while a:
         inp=int(input())
         if inp>=1 and inp<=n:
             a=False
     return inp
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     while ((len(human)!=0) and (len(dealer)!=0)):
         print("Your turn")
         print("Your current deck of cards is: ")
         print_deck(human)
         print("I have ",(len(dealer))," cards. If 1 stands for my first card and",len(dealer),
               " for my last card, which of my cards would you like?")
         print("Give me an integer between 1 and ",len(dealer),":",)
         a=get_valid_input(len(dealer))
         if a==1:
             print("You asked for my",a ,"st card.")
         elif a==2:
             print("You asked for my",a ,"nd card.")
         elif a==3:
             print("You asked for my",a ,"rd card.")
         else:
             print("You asked for my",a ,"th card.")
         print("Here it is. It is ", dealer[a-1])
         print("With ",dealer[a-1]," added, your current deck of cards is:")
         human.append(dealer[a-1])
         dealer.remove(dealer[a-1])
         print_deck(human)
         print("And after discarding pairs and shufing, your deck is:")
         remove_pairs(human)
         shuffle_deck(human)
         print_deck(human)
         wait_for_player()
         if((len(human)!=0) and (len(dealer)!=0)):
             print("My turn ")
             b=random.randint(1,len(human))
             if b==1:
                 print("I took your",b ,"st card.")
             elif b==2:
                 print("I took your",b ,"nd card.")
             elif b==3:
                 print("I took your",b ,"rd card.")
             else:
                 print("I took your",b,"th card.")
             dealer.append(human[b-1])
             human.remove(human[b-1])
             remove_pairs(dealer)
             shuffle_deck(dealer)
             wait_for_player()
     if len(human)==0:
         print("Ups. You do not have any more cards")
         print("Congratulations! You, Human, win")
     elif(len(dealer)==0):
         print("Ups. I do not have any more cards")
         print("You lost! I, Robot, win")
           

# main
play_game()
