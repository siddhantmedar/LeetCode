class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = sqrt(num)
        
        return int(x)**2 == int(num)