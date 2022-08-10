class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) < n-1:
            return -1
        
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
            
        for i in range(n):
            find(i)
            
        print(parent)
        return len(set([v for _,v in parent.items()]))-1