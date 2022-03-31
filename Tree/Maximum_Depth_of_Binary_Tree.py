def maxDepth(root):
        def max_depth(root):
            if root is None:
                return 0
            l=max_depth(root.left)
            r=max_depth(root.right)
            return 1+max(l,r)
        return max_depth(root)