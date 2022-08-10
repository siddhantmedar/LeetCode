class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            setX = find(x)
            setY = find(y)
            
            if setX != setY:
                parent[setY] = setX
                
        m,n = len(nums), len(nums [0])
        parent = {i:i for i in range(len(nums))}
        
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 1:
                    union(i,j)
                    
        return sum([1 for k,v in parent.items() if k == v])