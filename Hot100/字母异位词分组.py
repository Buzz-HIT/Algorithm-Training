from collections import defaultdict
def groupAnagrams(strs):
    strDict = defaultdict(list)
    sortStr = []
    for s in strs:
        sortS = ''.join(sorted(s)) ## sorted出来的是list
        sortStr.append(sortS)
    for i in range(len(strs)):
        strDict[sortStr[i]].append(strs[i])
    ans = list(strDict.values())
    return ans

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
