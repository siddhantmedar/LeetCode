class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            cnt = 0
            
            while n:
                cnt+=(n&1)
                n>>=1
                
            return cnt
        
        
        result = []
        
        
        for i in range(n+1):
            result.append(count(i))
            
        return result
        