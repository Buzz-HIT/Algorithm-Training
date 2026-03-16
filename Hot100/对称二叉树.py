class Solution(object):
    def compare(self, left, right):
        if left == None and right == None:
            return True
        if left == None and right != None:
            return False
        if left != None and right == None: 
            return False   
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        return self.compare(root.left, root.right)