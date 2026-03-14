def findAnagrams(s, p):
    from collections import defaultdict
    hashS = defaultdict(int)
    hashP = defaultdict(int)
    ans = []
    if len(s) < len(p):
        return ans
    for i in range(len(p)):
        hashP[p[i]] += 1
    for i in range(0, len(p)):
        hashS[s[i]] += 1
    left = 0 
    right = len(p) - 1
    while right < len(s):
        if hashP == hashS:
            ans.append(left)
        right += 1
        if right < len(s):
            hashS[s[right]] += 1
        hashS[s[left]] -= 1
        if hashS[s[left]] == 0:
            hashS.pop(s[left])
        left += 1
    return ans

s = "abab"
p = "ab"

print(findAnagrams(s, p))