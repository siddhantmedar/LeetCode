class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(31, -1, -1):
            result<<=1
            mask = n&1
            n>>=1
            result|=mask
            
        return result
            
            