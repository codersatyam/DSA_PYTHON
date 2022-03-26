def robber(nums,n,dp):
    if n==0:
        return nums[0]
    if n<0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=max(nums[n]+robber(nums,n-2,dp),robber(nums,n-1,dp))
        return dp[n]
def rob(nums):
        dp=[-1]*(len(nums))
        return robber(nums,len(nums)-1,dp)
        