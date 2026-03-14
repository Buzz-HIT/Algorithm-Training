# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        dp = self.robTree(root)
        return max(dp[0], dp[1])
    def robTree(self, root):
        if root == None:
            return (0, 0)
        left = self.robTree(root.left)
        right = self.robTree(root.right)

        val0 = left[1] + right[1] + root.val #抢
        val1 = max(left[0], left[1]) + max(right[0], right[1]) # 不抢

        return (val0, val1)
        