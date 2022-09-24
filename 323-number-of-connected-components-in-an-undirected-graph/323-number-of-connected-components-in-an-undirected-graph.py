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
                if size[setX] >= size[setY]:
                    size[setX]+=size[setY]
                    parent[setY] = setX
                    
                else:
                    size[setY]+=size[setX]
                    parent[setX] = setY
                    
        parent = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}
        
        for u,v in edges:
            union(u,v)
        
        print(parent)
        print(size)
        
        return sum([1 for k,v in parent.items() if k ==  v])
    