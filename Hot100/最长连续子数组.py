def longestConsecutive(nums):
    num_set = set(nums)

    maxLength = 0

    for num in num_set:
        if num - 1  not in num_set:
            curLength = 1
            curNum = num
            while curNum + 1 in num_set:
                curLength += 1
                curNum += 1
            
            maxLength = max(maxLength, curLength)
    return maxLength
                