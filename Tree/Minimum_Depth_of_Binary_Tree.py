def minDepth(root):
        def min_height(root):
            if not root:
                return 0
            else:
                l=min_height(root.left)
                r=min_height(root.right)
                # SKEWED CONDITION : 
                if l == 0 or r == 0:
                    return 1+max(l,r)
                return 1+min(l,r)
        return min_height(root)    
                
        