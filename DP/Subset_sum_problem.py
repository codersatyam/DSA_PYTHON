def isSubsetSum (N, arr, summ):
        dp=[[0 for _ in range(summ+1)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(summ+1):
                if i==0 and j==0:
                    dp[i][j]=1
                elif i==0:
                    dp[i][j]=0
                elif j==0:
                    dp[i][j]=1
                else:    
                    if arr[i-1]<=j:
                           dp[i][j]=max(dp[i-1][j-arr[i-1]],dp[i-1][j])
                    else:
                        dp[i][j]=dp[i-1][j]        
        return dp[N][summ]