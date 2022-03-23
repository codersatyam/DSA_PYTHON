def jump(nums):
    dp=0
    for i in range(len(nums)):
        if dp>i:
            return False
        dp=max(dp,i+nums[i])    
    return True    