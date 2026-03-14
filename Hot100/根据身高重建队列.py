def buildHeightque(people):
    people.sort(key=lambda x : (-x[0], x[1]))
    que = []
    for p in people:
        que.insert(p[1], p)
    return que

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(buildHeightque(people))