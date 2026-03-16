class Solution(object):
    def __init__(self):
        self.lettermap = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.result = []
        self.path = ""
    def backTrack(self, digits, index):
        if index == len(digits):
            self.result.append(self.path)
            return
        letterIndex = int(digits[index])
        letterList = list(self.lettermap[letterIndex])
        for i in range(len(letterList)):
            self.path += letterList[i]
            self.backTrack(digits, index+1)
            self.path = self.path[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.backTrack(digits, 0)
        return self.result
    
digits = "23"
solution = Solution()
print(solution.letterCombinations(digits))
            
