# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = None
        
        low, high = 1, n
        
        while low<=high:
            mid = (low+high)>>1
            
            if isBadVersion(mid):
                result = mid
                high = mid-1
                
            else:
                low = mid+1
                
        return result