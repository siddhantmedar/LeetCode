class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = {i:(0,0) for i in range(1, n+1)}
        
        for u,v in trust:
            indegree, outdegree = mp[v]
            mp[v] = (indegree+1, outdegree)
            indegree, outdegree = mp[u]
            mp[u] = (indegree, outdegree+1)
            
        cand = []
        
        for k,v in mp.items():
            if v[0] == n-1 and v[1] == 0:
                cand.append(k)
     
        return cand[0] if len(cand) == 1 else -1