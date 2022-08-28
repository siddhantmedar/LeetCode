class Solution:
    def isArmstrong(self, n: int) -> bool:
        res = 0 
        ref = n
        p = len(str(n))
        
        while n:
            res += ((n%10)**p)
            n//=10
        
        return res == ref