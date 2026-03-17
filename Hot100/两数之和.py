def twoSum(nums, target):
    from collections import defaultdict
    numDict = defaultdict(int)
    result = []
    for i in range(len(nums)):
        index = numDict.get(target - nums[i], -1)
        if index != -1:
            result.append(index)
            result.append(i)
        else:
            numDict[nums[i]] = i
    return result

