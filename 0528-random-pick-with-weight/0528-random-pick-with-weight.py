class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = []
        
        sm = 0
        
        for i, ele in enumerate(self.w):
            sm+=ele
            self.prefix.append(sm)
       
    def pickIndex(self) -> int:
        target = self.prefix[-1]*random.random()
        
        for i,ele in enumerate(self.prefix):
            if target < ele:
                return i
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()