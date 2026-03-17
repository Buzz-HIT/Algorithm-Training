def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x:x[0])
    left = intervals[0][0]
    right = intervals[0][1]
    ans = []
    for i in range(1, len(intervals)):
        if intervals[i][0] <= right:
            right = max(right, intervals[i][1])
        else:
            ans.append([left, right])
            left = intervals[i][0]
            right = intervals[i][1]
    ans.append([left, right])

    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))