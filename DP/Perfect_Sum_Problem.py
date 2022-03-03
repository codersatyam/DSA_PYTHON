def perfectSum(ar, n, summ):
    mod=1e9+7
    dp=[[0 for _ in range(summ+1)] for _ in range(n+1)]
    zero=1
    arr=[]
    for i in ar:
        if i==0:
            zero=(zero*2)%mod
        else:      
            arr.append(i)
    n=len(arr)		        
    for i in range(n+1):
        for j in range(summ+1):
            if i==0 and j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=0
            elif j==0:
                dp[i][j]=1
            else:      
                    if arr[i-1]<=j:
                        dp[i][j]=(dp[i-1][j-arr[i-1]]+dp[i-1][j])%mod
                    else:
                        dp[i][j]=dp[i-1][j]%mod
    return int((dp[n][summ]*zero)%mod)
    