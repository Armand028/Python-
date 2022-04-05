def two_length_run(lis):
    '''
    (list)->(boolean)
    This function returns True if the given list has at least one run (of length at least two), and
    False otherwise
    '''
    t=False
    if len(lis)==0 or len(lis)==1:
        return t
    for i in range(0,len(lis)-1):
        if lis[i]==lis[i+1]:
            return True
    return t
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
l=[]
for x in raw_input:
    l.append(float(x))
print(two_length_run(l))
