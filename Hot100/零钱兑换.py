def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(0, amount + 1):
            if j - coins[i] >= 0:
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    if dp[amount] < float("inf"):
        return dp[amount]
    return -1

coins = [1]
amount = 0
print(coinChange(coins, amount))