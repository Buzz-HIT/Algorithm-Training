def moveZero(nums):
    slowIndex = 0
    fastIndex = 0
    while fastIndex < len(nums):
        if nums[fastIndex] != 0:
            nums[slowIndex] = nums[fastIndex]
            slowIndex += 1
        fastIndex += 1
    while slowIndex < len(nums):
        nums[slowIndex] = 0
        slowIndex += 1
    return nums

nums = [0,1,0,3,12]
print(moveZero(nums))