def findTargetSumWays(nums, target):
    numSum = sum(nums)
    if abs(target) > numSum:
        return 0
    amount = (numSum + target) // 2
    if (numSum + target) % 2 == 1:
        return 0 
    dp =[[0] * (amount + 1) for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = 1
    for j in range(1, amount + 1):
        if j == nums[0]:
            dp[0][j] = 1
    for i in range(1, len(nums)):
        for j in range(1, amount + 1):
            if j >= nums[i]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp[len(nums) - 1][amount]

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, 3))
