
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while True:
        pos = partition(nums, left, right)
        if pos == k - 1:
            return nums[pos]
        elif pos > k - 1:
            right -= 1
        else:
            left += 1
    

def partition(nums, left, right):
    index = left
    k = random.randint(left, right)

    privot = nums[k]
    nums[left], nums[k] = nums[k], nums[left]
    for i in range(left + 1, right + 1):
        if nums[i] > privot:
            index += 1
            nums[i], nums[index] = nums[index], nums[i]
    nums[index], nums[left] = nums[left], nums[index]
    return index

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print((findKthLargest(nums, k)))


def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        n = len(nums)
        for i in range(n - k + 1):
            ans = heapq.heappop(nums)
        return ans
        