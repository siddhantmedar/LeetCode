class MinStack:

    def __init__(self):
        self.st = []
        self.mn = None

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.mn = val
            
        else:
            if val <= self.mn:
                self.st.append(2*val-self.mn)
                self.mn = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        if self.st:
            ele = self.st.pop()
            
            if ele <= self.mn:
                self.mn = (2*self.mn)-ele
            
    def top(self) -> int:
        if self.st:
            if self.st[-1] > self.mn:
                return self.st[-1] 
            else:
                ele = self.st[-1]
                return (ele+(2*self.mn-ele))//2

    def getMin(self) -> int:
        return self.mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()