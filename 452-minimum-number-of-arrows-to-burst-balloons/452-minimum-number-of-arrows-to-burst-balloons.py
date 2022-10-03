class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        
        count = 1
        end = points[0][1]
        
        for p in points[1:]:
            if p[0] <= end:
                end = min(end, p[1])
                
            else:
                count+=1
                end = p[1]
                
        return count