#Armand GUIGMA
#Assignment 3


#####################################################################
#Question 2.1
########################################################################


def sum_odd_divisors(n):
    '''
    (int)->(int)
    This function returns the sum of all the postive odd divisors of n
    '''
    if n==0:
        return None
    else:
        sum=0
        for i in range(1,abs(n)+1):
            if(abs(n)%i==0 and i%2==1):
                sum=sum+i
    return sum
######################################################################
#Question 2.2
########################################################################

def series_sum():
    '''
    ()->(float or NOne)
    this function returns the somme of the following serie with a given n 1000 + 1/1**2 +
    1/2**2 + 1/3**2 + 1/4**2 + ... + 1/n**2 or None if n<0
    Preconditions: n must be positive
    '''
    n=int(input("Please enter a non-negative integer: "))
    if n<0:
        return None
    else:
        sum=1000
        for i in range(1,n+1):
            sum=sum+1/i**2
    return sum

#####################################################################
#Question 2.3
########################################################################

def pell(n):
    '''
    (int)->(int)
    this function helps approximate the value of √2
    Preconditions: n must be positive
    '''
    if n<0:
        return None
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        p0=1
        p1=2

        for i in range(3, n+1) :
            x = 2 * p1 + p0
            p0 = p1
            p1 = x
         
        return p1 
#####################################################################
#Question 2.4
########################################################################
def countMembers(s):
    '''
    str->int
    This function returns the number of characters in s that are extraordinary.
    a charactere is extraordinary if part of the followings characters lower case letter between e and j (inclusive), the upper
    case letters between F and X (inclusive), numerals between 2 and 6 (inclusive), and the exclamation point (!), comma (,),
    and backslash (\)
    '''
    count=0
    for i in s:
        if ( (i in 'efghij') or ('F' <= i and i <= 'X') or ('2' <= i and i <= '6') or (i in '!,\\')):
            count=count+1
    return count

#####################################################################
#Question 2.5
########################################################################

def casual_number(s):
    '''
    str->int
    this function return an integer representing a number in s
    '''
    ss=""
    d=0
    for i in range(len(s)):
        if s[i]=='-':
            d=d+1
        if (s[i]!='-' and s[i]!=','):
            ss=ss+s[i]
    if not ss.isdigit():
        return None
    elif d>1:
        return None
    else:
        ss=""
        for i in range(len(s)):
            if s[i]!=",":
                ss=ss+s[i]
    return int(ss)
    
#####################################################################
#Question 2.6
########################################################################
def alienNumbers(s):
	"""
		(str) -> int
		This function returns the value of string s
	"""

	return 1024*s.count("T")+598*s.count('y')+121*s.count('!')+42*s.count('a')+6*s.count('N')+ s.count('U')
    
#####################################################################
#Question 2.7
########################################################################
def alienNumbersAgain(s):
    """
    (str) -> int
    This function returns the value of string s
    """
	
    summ = 0
    for i in s:
            if i == "T":
                    summ += 1024
            elif i == 'y':
                    summ += 598
            elif i == "!":
                    summ += 121
            elif i == 'a':
                    summ += 42
            elif i == "N":
                    summ += 6
            elif i == "U":
                    summ += 1
    
    return summ
#####################################################################
#Question 2.8
########################################################################
def encrypt(s):
	'''
        (str) -> str
        returns a string which is the encrypted version of s
	'''
	
	reverse = s[::-1]
	half = len(s)//2
	first_part = reverse[:half]
	second_part = reverse[half:] 
	second_part2=second_part[::-1]
	
	response = ''
	for i in range(half):
		response=response+first_part[i]+second_part2[i]
	if len(second_part2) > len(first_part):
		response=response+second_part2[-1]
	return response
	return summ
#####################################################################
#Question 2.9
########################################################################
def oPify(s):

    '''(str)->str
        this function returns string s with letters op inserted in it
    '''
    if len(s)<=1:
        return s
    result=""
    for i in range(len(s)-1):
            a=s[i]
            b=s[i+1]
            if a.isalpha() and b.isalpha():
                    result=result+a
                    if a.isupper():
                            result=result+'O'
                    else:
                            result=result+'o'

                    if b.isupper():
                            result=result+'P'
                    else:
                            result=result+'p'
            else:result=result+a
    result=result+b
    return result
#####################################################################
#Question 2.10
########################################################################
def nonrepetitive(s):
    '''
    str->boolean
    This function returns True if s is nonrepetitive and False otherwise
    '''
    for i in range(len(s)):
            for d in range(1,(len(s)-i)//2 + 1):
                    if s[i:i+d]==s[i+d:i+2*d]:
                            print(s[i:i+d], s[i+d:i+2*d])
                            return False
    return True
