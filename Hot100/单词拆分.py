def wordBreak(s, wordDict):
    wordset = set(wordDict)
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] == 1 and s[j:i] in wordset:
                dp[i] = 1
                break # 能了就直接break 说明这个就可以了
    return True if dp[n] == 1 else False

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(wordBreak(s, wordDict))