class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        result = 0
        
        end = intervals[0][1]
        
        for s,e in intervals[1:]:
            if s>=end:
                end = e
                
            else:
                result+=1
                end = min(end, e)
                
        return result
        