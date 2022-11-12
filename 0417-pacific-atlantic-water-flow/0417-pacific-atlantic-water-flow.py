class Solution:
    def pacificAtlantic(self, nums: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,pre,st):
            if i<0 or i>=M or j<0 or j>=N or (i,j) in st or nums[i][j] < pre:
                return
            
            st.add((i,j))
            
            for dx,dy in directions:
                dx+=i
                dy+=j
            
                dfs(dx,dy,nums[i][j],st)
            
            
        M,N = len(nums), len(nums[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        pac, atl = set(), set()
        
        for i in range(M):
            dfs(i,0,nums[i][0],pac)
            dfs(i,N-1,nums[i][N-1],atl)
            
        for j in range(N):
            dfs(0,j,nums[0][j],pac)
            dfs(M-1,j,nums[M-1][j],atl)
       
        return list(pac.intersection(atl))