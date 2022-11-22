class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x,y):
            setX, setY = find(x), find(y)
            
            if setX != setY:
                parent[setY] = setX
        
        
        if len(edges) < n-1:
            return -1
        
        parent = {x:x for x in range(n)}
        
        for u,v in edges:
            union(u,v)
        
        return sum([1 for k,v in parent.items() if k==v])-1