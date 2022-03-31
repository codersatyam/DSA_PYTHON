def countNodes(root):
        # time complexity(logNlogN)
        # will at least walk through one perfect binary tree
        
        left, right = root, root
        leftHeight, rightHeight = 0, 0
        
        while left:
            leftHeight += 1
            left = left.left

        while right:
            rightHeight += 1
            right = right.right

        if leftHeight == rightHeight: # perfect binary tree
            return pow(2, leftHeight) - 1

        # traverse through binary tree and count
        return 1 + countNodes(root.left) + countNodes(root.right)