class Solution:
    def countBits(self, n: int) -> List[int]:
        def solve(n):
            count = 0
            
            while n:
                count+=(n&1)
                n>>=1
                
            return count
        
        res = []
        
        for i in range(n+1):
            res.append(solve(i))
            
        return res
        