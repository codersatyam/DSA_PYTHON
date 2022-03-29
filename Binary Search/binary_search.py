def binary(nums,start,end,target):
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end=mid-1
        else:
            start=mid+1