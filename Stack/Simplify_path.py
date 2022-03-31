def simplifyPath(path):
        new_str=path.split("/")
        stack=[]
        for i in new_str:
            if i=="." or i=="":
                continue
            elif stack and i=="..":
                stack.pop()
            elif i!="..":
                stack.append(i)       
        x="/".join(stack)
        return "/"+x