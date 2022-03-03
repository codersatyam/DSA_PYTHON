###########    STACK     ###########
####### First In First Out  ########
####### Using list in python #######

stack=[]       ## Empty stack declaration
stack.append() ## add element to the top to stack 
stack.pop()    ## remove element from top of the stack
stack[-1]      ## reterive top element of stack
if len(stack)==0: ## check stack is empty or not 
    print("empty")


##########   Using oops  ###########
    
class stack:
    def __init__(self):
        self.s=[]

    def push(self,x):
        self.x=x
        self.s.append(self.x)

    def pop(self):
        if len(self.s)==0:
            print("stack is empty")
        else:    
            self.s.pop()   

    def top(self):
        if len(self.s)==0:
            print("stack is empty")
        else:    
            print(self.s[-1])   


s1=stack()
s1.push(4)
s1.push(5)
s1.push(8)
s1.top()
s1.pop()
s1.push(1)
s1.pop()
s1.pop()
s1.top()
s1.pop()
s1.pop()


