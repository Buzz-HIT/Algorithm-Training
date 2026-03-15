def backTrack(nums, target, startIndex, path):
    if target == 0:
        result.append(path[:])
        return
    if target < 0:
        return
    for i in range(startIndex, len(nums)):
        path.append(nums[i])
        target -= nums[i]
        backTrack(nums, target, i, path)
        target += nums[i]
        path.pop()
    return
result = []
nums = [2,3,6,7]
target = 7
backTrack(nums, target, 0, [])
print(result)



