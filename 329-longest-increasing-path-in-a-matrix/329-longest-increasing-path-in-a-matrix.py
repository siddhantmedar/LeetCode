class Solution:
    def longestIncreasingPath(self, nums: List[List[int]]) -> int:
        def dfs(i,j,x,y):
            if i<0 or i>=M or j<0 or j>=N:
                return 0
            
            if (i,j) in visited:
                return dp[i][j]
            
            visited.add((i,j))
            
            res = 0
            
            for dx, dy in directions:
                if 0<=dx+i<M and 0<=dy+j<N and nums[dx+i][dy+j] > nums[i][j]:
                    res = max(res, dfs(dx+i, dy+j, i, j))
            
            dp[i][j] = max(res+1, dp[i][j])
            
            return dp[i][j]
        
        
        M,N = len(nums), len(nums[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        
        res = float("-inf")
        
        dp = [[1 for _ in range(N)] for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                result = dfs(i,j,i,j)
                
                res = max(res, result)
                
        return res
                