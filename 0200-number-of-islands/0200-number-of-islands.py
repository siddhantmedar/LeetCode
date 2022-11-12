class Solution:
    def numIslands(self, nums: List[List[str]]) -> int:
        def bfs(i,j):
            q = deque([(i,j)])
            
            while q:
                n = len(q)
                
                for k in range(n):
                    i,j = q.popleft()
                    
                    if i<0 or i>=M or j<0 or j>=N or nums[i][j] == "0":
                            continue
                        
                    nums[i][j] = "0"
                    
                    for dx,dy in directions:
                        dx+=i
                        dy+=j
                        
                        q.append((dx,dy))
                
        M,N = len(nums), len(nums[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        cnt = 0
        
        for i in range(M):
            for j in range(N):
                if nums[i][j] == "1":
                    bfs(i,j)
                    cnt+=1
                    
        return cnt