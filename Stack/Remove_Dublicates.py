from collections import Counter
def removeDuplicateLetters(s):
        count=Counter(s)
        stack=[]    
        for i in range(len(s)) :
            if s[i] in stack:
                count[s[i]]-=1
                continue
            while (stack and stack[-1]>s[i] and count[stack[-1]]>0):
                   stack.pop()
            count[s[i]]-=1        
            stack.append(s[i])              
        return "".join(stack)   