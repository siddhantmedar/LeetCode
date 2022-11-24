class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        res = [intervals[0]]
        
        for start,end in intervals[1:]:
            if res[-1][1] >= start:
                last = res.pop()
                start = min(start,last[0])
                end = max(end, last[1])
                
            res.append([start,end])
            
        return res