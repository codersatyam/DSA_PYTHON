def isBalanced(root):
        def is_balance(root):
            if root is None:
                return 0
            l=is_balance(root.left)
            r=is_balance(root.right)
            if l==-1 or r==-1:
                return -1
            if abs(l-r)>1:
                return -1
            return 1+max(l,r)
        if root is None:
            return True
        return is_balance(root)!=-1