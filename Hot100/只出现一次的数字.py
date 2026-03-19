def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result