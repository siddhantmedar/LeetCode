class Solution:
    def pacificAtlantic(self, nums: List[List[int]]) -> List[List[int]]:
        def solve():
            def bfs(i,j,pre,st):
                q = deque([(i,j,pre,st)])
                
                while q:
                    n = len(q)
                    
                    for k in range(n):
                        i,j,pre,st = q.popleft()
                        if i<0 or i>=M or j<0 or j>=N or (i,j) in st or nums[i][j] < pre:
                                continue
                        
                        st.add((i,j))
                        
                        for dx,dy in directions:
                            dx+=i
                            dy+=j
                            
                            q.append((dx,dy,nums[i][j], st))
            
            
            M,N = len(nums), len(nums[0])
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            pac, atl = set(), set()
        
            for i in range(M):
                bfs(i,0,nums[i][0],pac)
                bfs(i,N-1,nums[i][N-1],atl)
            
            for j in range(N):
                bfs(0,j,nums[0][j],pac)
                bfs(M-1,j,nums[M-1][j],atl)
                
            return list(pac.intersection(atl))
        
        return solve()