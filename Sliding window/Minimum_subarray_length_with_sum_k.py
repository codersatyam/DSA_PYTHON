def minSubArrayLen(target,nums):
        window_start=0
        minimum_length=len(nums)
        current_sum=0
        for window_end in range(len(nums)):
            current_sum+=nums[window_end]
            while current_sum>=target:
                minimum_length=min(minimum_length,window_end-window_start+1)
                current_sum-=nums[window_start]
                window_start+=1
        if sum(nums)>=target:        
            return minimum_length         
        else:
            return 0