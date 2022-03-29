def rotate(nums):
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]<nums[0]:
                end=mid
            else:
                start=mid+1
        if nums[start]<nums[0]:
            return start
        else:
            return 0