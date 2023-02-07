class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx = None
        dist = float("inf")
        
        for idxx,(i,j) in enumerate(points):
            
            if (i,j) == (x,y):
                return idxx
            
            if i == x or j == y:
                tmp = abs(x-i)+abs(y-j)

                if tmp < dist:
                    dist = tmp
                    idx = idxx

                elif tmp == dist and idxx < idx:
                    idx = idxx
                    dist = tmp
        
        return idx if idx != None else -1