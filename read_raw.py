
def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''
    l=sorted(l)
    clean_board=[]
    for i in range(len(l)):
        a=l[i]
        if a!="*":
            clean_board.append(a)
    l=clean_board
    for c in range(len(l)):
        num=l.count(l[c])
        if num%2==1:
            l[c]=" "
    clean_board=l
    l_l=[]
    for i in clean_board:
        if i!=" ":
            l_l.append(i)
    clean_board=l_l
    return clean_board
    


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    t=True
    if l==[]:
        return True
    else:
        for y in range(len(l)):
            num=l.count(l[y])
            if num%2==1:
                t=False
                return t
        return t
    
#main
file=input("Enter the name of the file: ")
file=file.strip()
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * but is not rigorous and it has "+str(len(b))+" characters.")
     
