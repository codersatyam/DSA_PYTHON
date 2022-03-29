def subarray(arr):
    l=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            l.append(arr[i:j+1])
    return l        

arr=[1,2,3,4,5]
output=subarray(arr)
print(output)