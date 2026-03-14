def maxSubsequece(nums):
    dp = [1] * len(nums)
    if len(nums) <= 1:
        return len(nums)
    result = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        if result < dp[i]:
            result = dp[i]
    return result