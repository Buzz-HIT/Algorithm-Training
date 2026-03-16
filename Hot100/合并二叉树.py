def preTree(root1, root2):
        if root1 == None and root2 == None:
            return None
        if root1 == None and root2 != None:
            return root2
        if root1 != None and root2 == None:
            return root1
        root1.val += root2.val
        root1.left = preTree(root1.left, root2.left)
        root1.right = preTree(root1.right, root2.right)
        return root1 

def mergeTrees(root1, root2):
    """
    :type root1: Optional[TreeNode]
    :type root2: Optional[TreeNode]
    :rtype: Optional[TreeNode]
     """
    root = preTree(root1, root2)
    return root   