class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            result = 0
            
            while n:
                result+=(n&1)
                n>>=1
                
            return result
        
        result = []
        
        for i in range(0, n+1):
            result.append(count(i))
            
        return result