def longest_run(lis):
    '''
    (list)->(int)
    This function returns the longest_run (longest sequence of consecutive repeated values)
    '''
    
    i = 0
    max = 1
    if len(lis)==0:
        return 0
    while i < len(lis)-1 :
        temp = 1
        while  i < len(lis)-1 and lis[i] == lis[i+1]:
           temp = temp + 1
           i = i + 1
        if temp > max:
           max = temp  
        i = i + 1
    
    return max

s = input('Please input a list of numbers separated by space: ').strip().split()
a=[]
for item in s:
     a.append(float(item))

print(longest_run(a))
