def scoreOfParentheses(s):
        stack=[]
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                if stack[-1]=="(":
                    stack.pop()
                    stack.append(1)
                else:    
                    summ=0
                    while stack and stack[-1]!="(":
                        summ+=stack.pop()
                    stack.pop()    
                    stack.append(2*summ)    
                    summ=0
        return sum(stack)        
                
        