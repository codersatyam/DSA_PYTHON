def largestRectangleArea(nums):
        def nearestsmallestelement(nums):
            ans=[]
            stack=[]
            for i in range(len(nums)-1,-1,-1):
                while len(stack)!=0 and stack[-1][1]>=nums[i]:
                    stack.pop()
                if len(stack)==0:
                    ans.append(len(nums))    
                else:
                    ans.append(stack[-1][0])
                stack.append([i,nums[i]])    
            ans.reverse()    
            return ans 
        def nearestsmallestelementleft(nums):
            ans=[]
            stack=[]
            for i in range(len(nums)):
                while len(stack)!=0 and stack[-1][1]>=nums[i]:
                    stack.pop()
                if len(stack)==0:
                    ans.append(-1)    
                else:
                    ans.append(stack[-1][0])
                stack.append([i,nums[i]])    
            return ans
        NSR=nearestsmallestelement(nums)
        NSL=nearestsmallestelementleft(nums)
        area=[]
        for i  in range(len(nums)):
             area.append(nums[i]*(NSR[i]-NSL[i]-1))                                
        return max(area)                         
                                

    