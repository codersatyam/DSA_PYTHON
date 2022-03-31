def threeSum(nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                l=i+1
                r=len(nums)-1
                summ=0-nums[i]
                while l<r:
                    if nums[l]+nums[r]==summ:
                        ans.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<summ:
                        l+=1
                    else:
                        r-=1
        return ans 