def maxProfit(prices):
    dp = [[0] * 4 for _ in range(len(prices))] # 0:买入;1:今天卖出;2：冷冻期;3：过冷冻期
    dp[0][0] = -prices[0]

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][2], dp[i - 1][3]) - prices[i])
        dp[i][1] = dp[i - 1][0] + prices[i]
        dp[i][2] = dp[i - 1][1]
        dp[i][3] = max(dp[i - 1][2], dp[i - 1][3])
    return max(dp[len(prices) - 1][1], dp[len(prices) - 1][2], dp[len(prices) - 1][3])