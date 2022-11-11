class Solution:
    def hammingWeight(self, n: int) -> int:
        def count(n):
            cnt = 0
            
            while n:
                cnt+=(n&1)
                n>>=1
                
            return cnt
        
        return count(n)
        