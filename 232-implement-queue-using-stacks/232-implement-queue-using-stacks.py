class MyQueue:

    def __init__(self):
        self.st = []
        self.helper = []
        
    def push(self, x: int) -> None:
        if not self.st:
            self.st.append(x)
            
        else:
            while self.st:
                self.helper.append(self.st.pop())
            
            self.st.append(x)
            
            while self.helper:
                self.st.append(self.helper.pop())
            
    def pop(self) -> int:
        if self.st:
            return self.st.pop()

    def peek(self) -> int:
        if self.st:
            return self.st[-1]

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()