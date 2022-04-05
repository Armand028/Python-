import random
#Armand Guigma

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    network2=[]
    # YOUR CODE GOES HERE
    for i in range(1,len(friends)):
        network2.append(friends[i].split(" "))
    numberDone=[]
    for y in range(0,len(network2)):
        liste=[]
        number=network2[y][0]
        if((y!=len(network2)-1) and (network2[y+1][0]!=network2[y][0])):
            for x in range(0,len(network2)):
                if(network2[x][0]==number):
                    liste.append(int(network2[x][1]))
                if(network2[x][1]==number):
                    liste.append(int(network2[x][0]))
            elem=(int(number),sorted(liste))
            network.append(elem)
            network=network
            numberDone.append(number)
        elif(y==len(network2)-1):
            for x in range(1,len(network2)):
                if(network2[x][0]==number):
                    liste.append(int(network2[x][1]))
                if(network2[x][1]==number):
                    liste.append(int(network2[x][0]))
            elem=(int(number),sorted(liste))
            network.append(elem)
            numberDone.append(number)
            
    for un in range(int(friends[0])):
        liste=[]
        if(str(un) not in numberDone):
            for yx in range(len(network2)):
                if(network2[yx][1]==str(un)):
                    liste.append(int(network2[yx][0]))
            elem=(un,sorted(liste))
            network.append(elem)
            numberDone.append(un)  
    return sorted(network)

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    indi1=-2
    indi2=-2
    # YOUR CODE GOES HERE
    for s in range(len(network)):
        if (network[s][0]==user1):
            indi1=s
        if (network[s][0]==user2):
            indi2=s  
    for i in network[indi1][-1]:
        if i in network[indi2][-1]:
            common.append(i)
    return sorted(common)

def checkFriendFriends(user1,user2,network):
    '''
    (int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted
    This function returns True if one of user1'friends is friend with at least one of user2'friend and False otherwise.
    '''
    indi1=-2
    indi2=-2
    # YOUR CODE GOES HERE
    for s in range(len(network)):
        if (network[s][0]==user1):
            indi1=s
        if (network[s][0]==user2):
            indi2=s 
    for i in range(len(network[indi1][-1])):
        frien=network[indi1][-1][i]
        for y in range(len(network[indi2][-1])):
            
            a=getCommonFriends(network[indi2][-1][y],frien,network)
            for i in a:
                if len(a)!=0:
                    return True
    return False
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    liste=[]
    for i in range(len(network)):
        if (network[i][0]!=user) and (user not in network[i][-1]) and (checkFriendFriends(user,network[i][0],network)):
            x=len(getCommonFriends(user,network[i][0],network))
            u=(network[i][0],x)
            liste.append(u)
    if len(liste)==0:
        return None
   # elif len(liste)==1:
       # return liste[0][0]
    else:
        max=liste[0][-1]
        ID=liste[0][0]
        for i in range(len(liste)):
            if(liste[i][-1]>max):
                max=liste[i][-1]
                ID=liste[i][0]
            elif(liste[i][-1]==max):
                if(ID>liste[i][0]):
                    ID=liste[i][0]
        return ID

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    count=0
    for i in range(len(network)):
        if len(network[i][-1])>=k:
            count=count+1
    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    max=len(network[0][-1])
    for i in range(len(network)):
        if len(network[i][-1])>=max:
            max=len(network[i][-1])
    return max
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    a=maximum_num_friends(network)
    for i in range(len(network)):
        if len(network[i][-1])==a:
            max_friends.append(network[i][0])
    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    somme=0
    for i in range(len(network)):
        somme=somme+len(network[i][-1])
    return somme/len(network)
    # YOUR CODE GOES HERE

    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    a=True
    for i in range(len(network)):
        a=True
        w=network[i][0]
        for y in range(len(network)):
            if(y!=i):
                if w not in network[y][-1]:
                    a=False
        if(a==True):
            return a
            
    return a
        
    # YOUR CODE GOES HERE



####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    a=True
    while a:
        l=input("Enter an integer for a user ID: ").strip()
        try:
            l=int(l)
            a=True
            #if (l.is_integer()):
            for y in range(len(network)):
                if l==network[y][0]:
                    a=False
                    return l
            if a==True:
                print("That user ID does not exist. Try again.")
        except:
            print("That was not an integer. Please try again.")
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
