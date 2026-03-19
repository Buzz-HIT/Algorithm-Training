# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def maxGain(node):
            if node == None:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            printNewpath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, printNewpath)

            return node.val + max(leftGain, rightGain)
        
        maxGain(root)

        return self.maxSum