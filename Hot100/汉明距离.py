def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = x ^ y
        result = 0
        while s:
            result += s & 1
            s = s >> 1
        return result