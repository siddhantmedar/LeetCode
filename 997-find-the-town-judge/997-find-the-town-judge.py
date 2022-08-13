class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not len(trust):
            return -1 if n!=1 else 1
        
        mp = {i:(0,0) for i in range(1, 1001)}
        
        for u,v in trust:
            degree = mp[u]
            mp[u] = (degree[0],degree[1]+1)
            
            degree = mp[v]
            mp[v] = (degree[0]+1,degree[1])
            
        res = None
        
        for k,v in mp.items():
            if v[0] == n-1 and v[1] == 0:
                res = k
            
        return res if res else -1