class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c==0:
        #     return True
        
        for a in range(0,int(sqrt(c))+1):
            b = c-a**2
            
            if int(sqrt(b))**2 == int(b):
                return True
            
        return False