def maxPrduct(nums):
    if len(nums) == 0:
        return
    mindp = [0] * len(nums)
    maxdp = [0] * len(nums)
    mindp[0] = nums[0]
    maxdp[0] = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        maxdp[i] = max(nums[i], mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i])
        mindp[i] = min(nums[i], mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i])
        result = max(result, maxdp[i])
    return result    

nums = [-2,0,-1]
print(maxPrduct(nums))