def canPartition(nums):
    numSum = sum(nums)
    if numSum % 2 == 1:
        return False
    target = numSum // 2
    dp = [[False] * (target + 1) for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = True
    for j in range(target + 1):
        if j == nums[0]:
            dp[0][j] = True
    for i in range(1, len(nums)):
        for j in range(target + 1):
            if j >= nums[i]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(nums) - 1][target]

nums = [1,2,3,5]
print(canPartition(nums))