def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        cover = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False