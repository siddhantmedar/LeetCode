class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = []
        
        for i, ch in enumerate(s):
            if ch == c:
                indices.append(i)
                
        res = []
        
        for i, ch in enumerate(s):
            if ch == c:
                res.append(0)
                continue
            
            else:
                mn = float("inf")

                for d in indices:
                    mn = min(mn, abs(i-d))

                res.append(mn)
            
        return res