class Solution:
    def countBits(self, n: int) -> List[int]:
        def util(n):
            cnt = 0

            while(n):
                cnt+=(n&1)
                n>>=1

            return cnt
        
        res = []
        
        for i in range(n+1):
            res.append(util(i))
            
        return res