import heapq
def topKFrenquence(nums, k):
    map_ = {}
    for i in nums:
        map_[i] = map_.get(i, 0) + 1
    
    que = []
    for key, freq in map_.items():
        heapq.heappush(que, (freq, key))
        if len(que) > k:
            heapq.heappop(que)
    result = [0] * k
    for i in range(k - 1, -1, -1):
        result[i] = heapq.heappop(que)[1]
    return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrenquence(nums, k))

