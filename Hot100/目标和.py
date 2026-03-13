def findTargetSumWays(nums, target):
    numSum = sum(nums)
    if abs(target) > numSum:
        return 0
    amount = (numSum + target) // 2
    if (numSum + target) % 2 == 1:
        return 0 
    dp =[0] * amount + 1
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(amount, -1, -1):
            