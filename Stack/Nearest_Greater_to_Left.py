def nearestgreaterelementleft(nums):
    ans=[]
    stack=[]
    for i in range(len(nums)):
        while len(stack)!=0 and stack[-1]<=nums[i]:
            stack.pop()
        if len(stack)==0:
            ans.append(-1)    
        else:
            ans.append(stack[-1])
        stack.append(nums[i])    
    return ans    

x=[1,3,2,4]
xx=nearestgreaterelementleft(x)
print(xx)