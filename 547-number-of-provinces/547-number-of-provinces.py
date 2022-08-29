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
                
                
        parent = {x:x for x in range(len(nums))}
        
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j]:
                    union(i,j)
        
        return sum([1 for k,v in parent.items() if k==v])