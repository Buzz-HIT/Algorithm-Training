def dailyTemperature(nums):
    stack = []
    ans = [0] * len(nums)
    for i in range(len(nums)):
        if len(stack) == 0 or nums[i] > nums[stack[-1]]:
            while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                pos = stack.pop(-1)
                ans[pos] = i - pos
            stack.append(i)
        else:
            stack.append(i)
    return ans

nums = [30,60,90]
print(dailyTemperature(nums))