class Solution:
    def checkStraightLine(self, points: List[List[int]]) -> bool:
        if len(points) < 2:
            return False
        
        n = points[1][1]-points[0][1]
        d = points[1][0]-points[0][0]
        
        if n and d:
            ref = n/d
            
        elif d == 0:
            ref = float("inf")
            
        elif n == 0:
            ref = 0
            
        for i in range(len(points)-1):
            n = points[i+1][1]-points[i][1]
            d = points[i+1][0]-points[i][0]

            if n and d:
                slope = n/d

            elif d == 0:
                slope = float("inf")

            elif n == 0:
                slope = 0
                
            if slope != ref:
                return False
            
        return True