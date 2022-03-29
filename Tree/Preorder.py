def preorderTraversal(root):
    ans=[]
    def preorder(root,ans):
        if not root:
            return ans
        else:
            ans.append(root.val)
            if root.left is not None:
                preorder(root.left,ans)
            if root.right is not None:
                preorder(root.right,ans)
            return ans    
    return preorder(root,ans)        
                
                
        