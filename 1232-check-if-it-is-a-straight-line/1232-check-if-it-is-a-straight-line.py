class Solution:
    def checkStraightLine(self, points: List[List[int]]) -> bool:
        if len(points) < 2:
            return False
        
        n = points[1][1]-points[0][1]
        d = points[1][0]-points[0][0]
        
        if n == 0:
            slope = 0
            
        elif d == 0:
            slope = float("inf")
            
        else:
            slope = n/d
        
        for i in range(1, len(points)-1):
            n = points[i+1][1]-points[i][1]
            d = points[i+1][0]-points[i][0]
            
            if n == 0:
                tmp = 0
            
            elif d == 0:
                tmp = float("inf")

            else:
                tmp = n/d
            
            if tmp != slope:
                return False
            
        return True