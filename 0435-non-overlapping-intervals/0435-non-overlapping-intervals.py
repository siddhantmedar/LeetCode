class Solution:
    def eraseOverlapIntervals(self, x: List[List[int]]) -> int:
        x.sort(key=lambda x:x[1])
        
        cnt = 1
        end = x[0][1]
        
        for s,e in x[1:]:
            if s >= end:
                cnt+=1
                end = e
                
        return len(x)-cnt