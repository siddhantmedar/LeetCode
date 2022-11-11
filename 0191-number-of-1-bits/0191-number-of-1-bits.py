class Solution:
    def hammingWeight(self, n: int) -> int:
        def count(n):
            cnt = 0
            
            while n:
                n = n&(n-1)
                cnt+=1
                
            return cnt
        
        return count(n)
        