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
def binary(nums,start,end,target):
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1        
def search(nums,target):
        index=rotate(nums)
        x=binary(nums,0,index-1,target)
        y=binary(nums,index,len(nums)-1,target)
        return max(x,y)

            
                