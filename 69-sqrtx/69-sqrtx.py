class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        res = None
        
        while start <= end:
            mid = (start+end)>>1
            
            if mid*mid == x:
                return mid
            
            elif mid*mid < x:
                res = mid
                start = mid+1
                
            else:
                end = mid-1
                
        return res
        