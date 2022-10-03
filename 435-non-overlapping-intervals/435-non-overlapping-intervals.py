class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x:x[0])
        
        count = 0
        mn = nums[0][1]
        
        for start,end in nums[1:]:
            if start < mn:
                count+=1
                mn = min(mn, end)
                
            else:
                mn = end
                
        return count