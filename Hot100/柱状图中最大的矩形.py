def maxRectangle(heights):
    if len(heights) == 0:
        return 0
    result = 0
    singleStack = []
    heights.insert(0,0)
    heights.append(0)
    singleStack.append(0)
    for i in range(1, len(heights)):
        if heights[i] > heights[singleStack[-1]]:
            singleStack.append(i)
        elif heights[i] == heights[singleStack[-1]]:
            singleStack.pop()
            singleStack.append(i) # 如果都是相等的话那就要去找最远的，这样保证面积最大
        else:
            while singleStack and heights[i] < heights[singleStack[-1]]:
                mid = singleStack[-1]
                singleStack.pop()
                left = singleStack[-1] # 第一个小于
                right = i # 第一个大于，两者之间是全是大于mid的矩形，所以应该找到多少个大于mid的矩形w，此时mid是最小的，mid做高，w为宽
                h = heights[mid]
                w = right - left - 1
                result = max(h * w, result)
            singleStack.append(i)
    return result

# heights = [2,1,5,6,2,3]
heights = [2,4]

print(maxRectangle(heights)) 