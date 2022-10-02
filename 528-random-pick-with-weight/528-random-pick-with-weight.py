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
        
        start, end = 0, len(self.prefix)-1
        
        result = None
        
        while start <= end:
            mid = (start+end)>>1
            
            if self.prefix[mid] > target:
                result = mid
                end = mid-1
                
            else:
                start = mid+1
                
        return result
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()