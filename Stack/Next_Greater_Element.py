def nextgreaterelement(nums):   
    stack=[]
    NGL=[]
    for i in range(len(nums)-1,-1,-1):
        while len(stack)!=0 and stack[-1]<=nums[i]:
                stack.pop()
        if len(stack)==0:
                NGL.append([nums[i],-1])
        else:        
                NGL.append([nums[i],stack[-1]])  
        stack.append(nums[i])        
    return NGL.reverse()