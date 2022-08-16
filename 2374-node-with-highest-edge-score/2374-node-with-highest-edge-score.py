class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = {i:[] for i in range(len(edges))}
    
    
        for u, v in enumerate(edges):
            mp[v].append(u)
            
        mx = float("-inf")
        res = []
        
        for k,v in mp.items():
            if sum(v) > mx:
                mx = sum(v)
                res = [k]
            elif sum(v) == mx:
                res.append(k)
                
        return min(res)