class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        return log2(n)/2 == log2(n)//2