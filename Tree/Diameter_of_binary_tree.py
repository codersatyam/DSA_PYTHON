def diameterOfBinaryTree(self, root):
        self.maxx=0
        def height(root):
            if root is None:
                return 0
            l=height(root.left)
            r=height(root.right)
            self.maxx=max(self.maxx,l+r)
            return 1+max(l,r)
        height(root)    
        return self.maxx
        