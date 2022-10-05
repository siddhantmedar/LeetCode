class FreqStack:

    def __init__(self):
        self.freq = defaultdict()
        self.group =  defaultdict(deque)
        
        self.curr_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = 1+self.freq.get(val,0)
        
        f = self.freq[val]
        
        if f > self.curr_freq:
            self.curr_freq = f
            
        self.group[f].append(val)
        
        # print(self.group)
        
    def pop(self) -> int:
        result = self.group[self.curr_freq].pop()
        self.freq[result]-=1
        
        if not self.group[self.curr_freq]:
            self.curr_freq-=1

        # print(self.group)
        
        return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()