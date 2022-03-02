def printFirstNegativeInteger( A,K):
    l=[]
    ans=[]
    window_start=0
    for window_end in range(len(A)):
        if A[window_end]<0:
                l.append(A[window_end])
        if window_end-window_start+1==K:
            if len(l)==0:
                ans.append(0)
            else:
                ans.append(l[0])
                if A[window_start]==l[0]:
                   l.pop(0)
            window_start+=1    
    return ans       