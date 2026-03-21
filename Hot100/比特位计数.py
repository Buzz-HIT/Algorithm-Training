class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def countOnes(i):
            ans = 0
            while i:
                ans += 1
                i &= i - 1
            return ans
        res = []
        for i in range(n + 1):
            res.append(countOnes(i))
        return res
        