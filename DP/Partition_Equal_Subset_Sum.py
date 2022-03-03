def canPartition(nums):
        summ=sum(nums)
        if summ%2!=0:
            return False
        else:
            dp=[[0 for _ in range(summ//2+1)] for _ in range(len(nums)+1)]
            for i in range(len(nums)+1):
                for j in range(summ//2+1):
                    if i==0 and j==0:
                        dp[i][j]=0
                    elif i==0:
                        dp[i][j]=0
                    elif j==0:
                        dp[i][j]=1
                    else:
                        if nums[i-1]<=j:
                            dp[i][j]=max(dp[i-1][j-nums[i-1]],dp[i-1][j])
                        else:
                            dp[i][j]=dp[i-1][j]
            if dp[len(nums)][summ//2]==0:
                return False
            else:
                return True