class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        curNum = nums[0]
        curFre = 1
        for i in range(1, len(nums)):
            if nums[i] == curNum:
                curFre += 1
            else:
                curFre -= 1
                if curFre < 0:
                    curNum = nums[i]
                    curFre = 1
        return curNum