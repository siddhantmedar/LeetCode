class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x,y):
            setX = find(x)
            setY = find(y)
            
            if setX != setY:
                parent[setY] = parent[setX]
                return True
            
            return False
            
        parent = {i:i for i in range(1,len(edges)+1)}
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]