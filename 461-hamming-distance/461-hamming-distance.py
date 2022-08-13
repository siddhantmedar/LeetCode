class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y
        
        count = 0
        
        for i in range(32):
            count+=(res&1)
            res>>=1
        
        return count