def reverse(s1,s2):

    if(len(s1)<=1):
        return  

    while (len(s1)!=1):
        ele = s1.pop()
        s2.append(ele)
    
    lastelement = s1.pop()

    while(len(s2)!=0):
        ele = s2.pop()
        s1.append(ele)
    
    reverse(s1,s2)
    s1.append(lastelement)

s1 = [1,2,3,4]
s2 = []

reverse(s1,s2)
print(s1)