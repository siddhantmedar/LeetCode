class MinStack:

    def __init__(self):
        self.st = []
        self.helper = []
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.helper.append(val)

        else:
            self.st.append(val)
            
            if self.helper and self.helper[-1] >= val:
                self.helper.append(val)
        
    def pop(self) -> None:
        if self.st:
            item =self.st.pop()
            
            if self.helper and self.helper[-1] == item:
                self.helper.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()