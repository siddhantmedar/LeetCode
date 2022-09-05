class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = float("inf")
        res_idx = None
        
        for idx, p in enumerate(points):
            i, j = p[0], p[1]
            
            if i == x or j == y:
                if abs(i-x)+abs(j-y) < res:
                    res = abs(i-x)+abs(j-y)
                    res_idx = idx
                        
                elif abs(i-x)+abs(j-y) == res:
                    res_idx = min(res_idx, idx)
        
        return res_idx if res_idx  != None else -1