class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = {i:0 for i in range(len(edges))}
    
    
        for u, v in enumerate(edges):
            mp[v]+=u
            
        mx = float("-inf")
        res = []
        
        for k,v in mp.items():
            if v > mx:
                mx = v
                res = [k]
            elif v == mx:
                res.append(k)
                
        return min(res)