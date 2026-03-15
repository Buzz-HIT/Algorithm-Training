def trap(nums):
    singleStack = []
    if len(nums) <= 2:
        return 0
    ans = 0
    singleStack.append(0)
    for i in range(1, len(nums)):
        # print(singleStack)
        if nums[i] < nums[singleStack[-1]]:
            singleStack.append(i)
        else:
            while singleStack and nums[i] >= nums[singleStack[-1]]:
                    mid = singleStack.pop(-1)
                    # print(nums[mid])
                    if singleStack:
                        left = singleStack[-1]
                        right = i
                        height = min(nums[left], nums[right]) - nums[mid]
                        # print(nums[left], nums[right])
                        width = right - left - 1
                        ans += height * width
            singleStack.append(i)
    return ans
            
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(nums))
                
                        