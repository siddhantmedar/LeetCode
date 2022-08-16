class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x,y):
            setX = find(x)
            setY = find(y)
            
            if setX != setY:
                parent[setY] = setX
                return True
            else:
                return False
            
        parent = {i:i for i in range(n)}
        
        for u,v in edges:
            if not union(u,v):
                return False
    
        for i in range(n):
            find(i)
        
        return True if len(edges) == n-1 and len(set([v for k,v in parent.items()])) == 1 else False