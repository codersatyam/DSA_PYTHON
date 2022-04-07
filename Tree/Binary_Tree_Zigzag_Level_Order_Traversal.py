import collections
def zigzagLevelOrder(root):
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        ans=[]
        flag=0
        while queue:
            size=len(queue)
            temp=[]
            for _ in range(size):
                node= queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            if flag==1:
                ans.append(temp[::-1])    
                flag=0
            else:
                ans.append(temp)
                flag=1
        return ans      
                    
                
            
        