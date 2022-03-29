def subset(arr):
    l=[]
    for i in range(len(arr)+1):
        for j in range(i):
            l.append(arr[j:i])
    return l        

arr=[1,2,3,4,5]
output=subset(arr)
print(output)