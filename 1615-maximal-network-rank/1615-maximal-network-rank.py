class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0]*n
        adj = [[0]*n for _ in range(n)]
        
        for u,v in roads:
            if adj[u][v] or adj[v][u]:
                continue
                
            count[u]+=1
            count[v]+=1
            
            adj[u][v]=1
            adj[v][u]=1
            
        result = 0
        
        for u in range(n):
            for v in range(u+1,n):
                result = max(result,count[u]+count[v]-adj[u][v])
        
        return result