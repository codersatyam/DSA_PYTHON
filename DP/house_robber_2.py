def robber(nums):
    prev=nums[0]
    prev1=0
    for i in range(1,len(nums)):
        take=nums[i]
        if i>1:
            take+=prev1
        not_taken=0+prev
        cur=max(take,not_taken)
        prev1=prev
        prev=cur
    return prev     
        
        
def rob(nums):
        if len(nums)==1:
            return nums[0]
        temp1=nums.copy()
        temp1.pop()
        temp2=nums.copy()
        temp2.pop(0)
        ans1= robber(temp1)
        ans2= robber(temp2)
        return max(ans1,ans2)
        
        