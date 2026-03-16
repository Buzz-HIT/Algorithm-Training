# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        self.result.append(root.val)
        self.inOrder(root.right)
        
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.inOrder(root)
        for i in range(len(self.result) - 1):
            if self.result[i] >=  self.result[i + 1]:
                return False
        return True
        