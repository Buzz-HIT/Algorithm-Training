class MinStack(object):

    def __init__(self):
        self.minstack = []
        self.minNum = float("inf")
        self.minCount = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val < self.minNum:
            self.minNum = val
            self.minCount = 1
        elif val == self.minNum:
            self.minCount += 1
        self.minstack.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        
        cur = self.minstack.pop(-1)
        if cur == self.minNum:
            self.minCount -= 1
        if self.minCount == 0:
            self.minNum = float("inf")
            for i in range(len(self.minstack)):
                if self.minstack[i] < self.minNum:
                    self.minNum = self.minstack[i]
                    self.minCount = 1
                elif self.minstack[i] == self.minNum:
                    self.minCount += 1
        # print(self.minstack)
        # print(self.minNum)
        # print(self.minCount)
                
    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()