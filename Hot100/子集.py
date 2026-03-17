class Solution(object):
    def __init__(self):
        self.result = []
    def backTracking(self, nums, starIndex, path):
        if len(nums) == starIndex:
            return
        for i in range(starIndex, len(nums)):
            path.append(nums[i])
            self.result.append(path[:])
            self.backTracking(nums, i + 1, path)
            path.pop()
        return
    def subsets(self, nums):
        self.backTracking(nums, 0, [])
        return self.result
    
nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))