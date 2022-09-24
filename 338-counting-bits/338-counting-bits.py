class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            result = 0
            
            while n:
                n = n&(n-1)
                result+=1
                
            return result
        
        result = []
        
        for i in range(n+1):
            result.append(count(i))
            
        return result