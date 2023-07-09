class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x,y):
            setX = find(x)
            setY = find(y)
            
            if setX != setY:
                parent[setY] = setX
        
        
        parent = {x:x for x in range(n)}
        size = {x:1 for x in range(n)}
        
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for u, v in edges:
            union(u,v)
        
        return (sum([1 for k,v in parent.items() if k==v]))