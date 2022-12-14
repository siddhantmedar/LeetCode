class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0]*n
        mat = [[0]*n for _ in range(n)]
        
        for u,v in roads:
            if mat[u][v] or mat[v][u]:
                continue
            
            count[u]+=1
            count[v]+=1
            
            mat[u][v] = 1
            mat[v][u] = 1
            
        res = 0
        
        for i in range(n):
            for j in range(i+1,n):
                res = max(res,count[i]+count[j]-mat[i][j])
                
        return res