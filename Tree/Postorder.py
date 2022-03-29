def postorderTraversal(root):
        ans=[]
        def postorder(root,ans):
            if not root:
                return ans
            else:
                if root.left is not None:
                    postorder(root.left,ans)
                if root.right is not None:
                    postorder(root.right,ans)
                ans.append(root.val)    
                return ans    
        return postorder(root,ans)      
                     

        