class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(len(intervals)-1):
            curr, next = intervals[i], intervals[i+1]
                
            if next[0] < curr[1]:
                return False
            
        return True