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
                
        parent = {i:i for i in range(n)}
        
        for u,v in edges:
            union(u,v)
            
        count = 0
        
        for k,v in parent.items():
            if k == v:
                count+=1
                
        return count