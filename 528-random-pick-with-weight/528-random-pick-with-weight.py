class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.lst = w
        self.sm = 0
        
        for ele in w:
            self.sm+=ele
            
            self.prefix.append(self.sm)

    def pickIndex(self) -> int:
        target = random.random()*self.sm
        
        for i, ele in enumerate(self.prefix):
            if ele > target:
                return i
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()