import collections 
def levelOrder(root):
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        ans=[]
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
            ans.append(temp)    
        return ans            
        