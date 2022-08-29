class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(nums):
            start, end = 0, len(nums)-1
            
            res = -1
            while start <= end:
                mid = (start+end)>>1
                
                if nums[mid] < 0:
                    res = mid
                    end = mid-1
                
                elif nums[mid] >= 0:
                    start = mid+1
  
            return len(nums)-res if res != -1 else 0
        
        result = 0
        
        for row in grid:
            result+=search(row)
            
        return result