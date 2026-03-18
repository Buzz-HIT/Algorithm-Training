def maximalSquare(matrix):
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    result = 0
    for i in range(len(matrix)):
        # print(matrix[i][0])
        if matrix[i][0] == '1':
            dp[i][0] = 1
            result = 1
    for j in range(len(matrix[0])):
        if matrix[0][j] == '1':
            dp[0][j] = 1
            result = 1
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                result = max(result, dp[i][j])
    # print(dp)
    return result * result

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))

        