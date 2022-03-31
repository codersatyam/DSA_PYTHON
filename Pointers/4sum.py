def fourSum(nums,target):
        ans=set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                low=j+1
                high=len(nums)-1
                new_target=target-nums[i]-nums[j]
                while low<high:
                    two_sum=nums[low]+nums[high]
                    if new_target==two_sum:
                    
                        ans.add((nums[i],nums[j],nums[low],nums[high]))
                        low+=1
                        high-=1
                
                    elif two_sum<new_target:
                        low+=1
                    else:
                        high-=1
              
        return ans            