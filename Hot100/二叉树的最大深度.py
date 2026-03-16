def maxDepth(root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
