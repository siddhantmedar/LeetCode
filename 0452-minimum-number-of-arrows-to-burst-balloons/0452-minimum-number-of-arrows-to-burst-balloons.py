class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        
        count = 1
        limit = points[0][1]
        
        for start, end  in points[1:]:
            if start <= limit:
                continue
                
            else:
                limit = max(limit, end)
                count+=1
                
        return count