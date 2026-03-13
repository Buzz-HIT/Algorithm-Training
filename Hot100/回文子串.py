def countSubstrings(s):
    n = len(s)
    res = 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1): # 要写-1
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                    res += 1
                else:
                    if dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                        res += 1
    print(dp)
    return res

s = "aaa"

print(countSubstrings(s))
