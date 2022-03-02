def maxSlidingWindow(nums,k):
        maxx=list()
        window_start=0
        ans=[]
        maxx.append(nums[0])
        for window_end in range(1,len(nums)):
            while maxx and nums[window_end]>maxx[-1]:
                maxx.pop()
            maxx.append(nums[window_end]) 
            if window_end-window_start+1==k:
                ans.append(maxx[0])
                if nums[window_start]==maxx[0]:
                    maxx.pop(0)
                window_start+=1
        if k==1:
            return nums
        return ans