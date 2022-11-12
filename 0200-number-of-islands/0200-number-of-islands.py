class Solution:
    def numIslands(self, nums: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or nums[i][j] == "0":
                return
            
            nums[i][j] = "0"
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy)
                
        M,N = len(nums), len(nums[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        cnt = 0
        
        for i in range(M):
            for j in range(N):
                if nums[i][j] == "1":
                    dfs(i,j)
                    cnt+=1
                    
        return cnt