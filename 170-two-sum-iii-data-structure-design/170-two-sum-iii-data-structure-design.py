class TwoSum:

    def __init__(self):
        self.lst = []
        self.mp = defaultdict()
        self.idx = -1
        
    def add(self, number: int) -> None:
        self.idx+=1
        self.lst.append(number)
        self.mp[number] = self.idx
        
    def find(self, target: int) -> bool:
        for i, ele in enumerate(self.lst):
            if target-ele in self.mp and self.mp[target-ele] != i:
                return True
        
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)