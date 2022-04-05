def  number_divisible(lis,n):
    '''
    (list,int)->(int)
    This functions returns the number of elements in the list that are divisible by n
    '''
    number=0
    for i in lis:
        if i%n==0:
            number+=1
    return number
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
l=[]
for i in raw_input:
    l.append(int(i))
n=int(input("Please input an integer: "))
print(number_divisible(l,n))
