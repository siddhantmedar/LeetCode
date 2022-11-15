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
        
        low, high = 0, len(self.prefix)-1
        result = None
        
        while low<=high:
            mid = (low+high)>>1
            
            if self.prefix[mid] > target:
                result = mid
                high = mid-1
                
            else:
                low = mid+1
                
        return result
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()