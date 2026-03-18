def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        count = [0] * numCourses
        stack = []
        for pair in prerequisites:
            count[pair[1]] += 1
        for i in range(len(count)):
            if count[i] == 0:
                 stack.append(i)
        print(stack)
        ans = []
        while stack:
            cur = stack.pop(-1)
            print(stack)
            ans.append(cur)
            print(ans)
            for i in range(len(prerequisites)):
                if prerequisites[i][0] == cur:
                    count[prerequisites[i][1]] -= 1
                    if count[prerequisites[i][1]] == 0:
                        stack.append(prerequisites[i][1])
            # print(count)
        if len(ans) == numCourses:
             return True
        else:
             return False
        
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(canFinish(numCourses, prerequisites))        