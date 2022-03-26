def maxProfit( prices):
    ''' i=0
    j=1
    maxx=0
    while j!=len(prices):
        if (prices[j]-prices[i])<0:
            i=j
            j+=1
        else:
            maxx=max(maxx,(prices[j]-prices[i]))
            j+=1
    return maxx        '''
        
    p = [0]*len(prices)
    for i in range(1,len(prices)):
        p[i] = max(0, p[i-1]+prices[i]-prices[i-1])
        print(p)

    return max(p)
        