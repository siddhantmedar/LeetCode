class Solution:
    def countBits(self, n: int) -> List[int]:
        def bits(n):
            cnt = 0
            
            while n:
                n = n&(n-1)
                cnt+=1
            
            return cnt
        
        res = []
        
        for i in range(n+1):
            res.append(bits(i))
            
        return res