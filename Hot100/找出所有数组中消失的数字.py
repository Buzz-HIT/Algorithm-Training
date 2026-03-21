def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(len(nums)):
        index = nums[i] % n
        nums[index - 1] +=  n
    ans = []
    for i in range(len(nums)):
        if nums[i] <= n:
            ans.append(i + 1)
    return ans

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))