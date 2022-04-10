def start_binary(nums,target):
    start=0
    end=len(nums)-1
    r=-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            r=mid
            end=mid-1
        elif nums[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return r 

def end_binary(nums,target):
    start=0
    end=len(nums)-1
    e=-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            e=mid
            start=mid+1
        elif nums[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return e
            
        

def searchRange(nums,target):
        r=start_binary(nums,target)
        e=end_binary(nums,target)
        return (r,e)
        
        