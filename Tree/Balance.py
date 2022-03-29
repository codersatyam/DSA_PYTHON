class Solution:
    def isBalanced(self, root):
        self.ans=True
        def is_balance(root):
            if root is None:
                return 0
            l=is_balance(root.left)
            r=is_balance(root.right)
            if l==-1 or r==-1:
                self.ans=False
            if abs(l-r)>1:
                self.ans=False
            return 1+max(l,r)
        is_balance(root)
        return self.ans
        