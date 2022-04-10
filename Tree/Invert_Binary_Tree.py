def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is  None:
            return None
        new=TreeNode(root.val)
        new.left=self.invertTree(root.right)
        new.right=self.invertTree(root.left)
        return new
        