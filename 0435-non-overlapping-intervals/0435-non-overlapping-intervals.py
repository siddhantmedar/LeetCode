class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        
        count = 0
        
        ref = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < ref:
                count+=1
                ref = min(ref, end)
                
            else:
                ref = end
        
        return count