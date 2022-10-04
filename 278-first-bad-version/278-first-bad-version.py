# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = None
        
        start, end = 1, n
        
        while start <= end:
            mid = (start+end)>>1
            
            if isBadVersion(mid):
                result = mid
                end = mid-1
                
            else:
                start = mid+1
                
        return result