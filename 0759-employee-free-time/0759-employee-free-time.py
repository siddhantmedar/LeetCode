"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        
        intervals = sorted([interval for sc in schedule for interval in sc],key=lambda x:x.start)
        
        last = intervals[0].end
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            
            if curr.start > last:
                result.append(Interval(last,curr.start))
                
            last = max(last, curr.end)
            
        return result