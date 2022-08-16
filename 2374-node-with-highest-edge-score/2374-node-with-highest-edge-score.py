class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = {i:[] for i in range(len(edges))}
    
    
        for u, v in enumerate(edges):
            mp[v].append(u)
            
        mx = max([sum(v) for k,v in mp.items()])
        res = []
        
        for k,v in mp.items():
            if sum(v) == mx:
                res.append(k)
        
        print(mp)
        
        return min(res)
        
#         1,0,0,0,0,7,7,5
#         0 1 2 3 4 5 6 7
#         from idx to nums[idx]
        
#         0:1,2,3,4
#         1:0
#         7:5,6
#         5:7