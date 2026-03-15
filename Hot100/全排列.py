result = []
def backTrack(nums, used, path):
    if len(path) == len(nums):
        result.append(path[:])
        return
    for i in range(0, len(nums)):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(nums[i])
        backTrack(nums, used, path)
        used[i] = 0
        path.pop()
    return

nums = []
used = [0] * len(nums)
backTrack(nums, used, [])
print(result)