def substring(s):
    l=[]
    for i in range(len(s)):
        for j in range(i,len(s)):
            l.append(s[i:j+1])
    return l        

s="apple"    
output=substring(s)
print(output)