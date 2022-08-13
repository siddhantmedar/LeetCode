class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not len(trust):
            return -1 if n!=1 else 1
        
        mp = {i:(0,0) for i in range(1, 1001)}
        
        st = set([x for x in range(1,n+1)])
        
        for u,v in trust:
            degree = mp[u]
            mp[u] = (degree[0],degree[1]+1)
                
            degree = mp[v]
            mp[v] = (degree[0]+1,degree[1])
            
            if u in st:
                st.remove(u)
        
        if st and len(st) == 1:
            cand = [x for x in st][-1]
            return  cand if mp[cand][0] == n-1 and mp[cand][1] == 0 else -1
        
        return -1