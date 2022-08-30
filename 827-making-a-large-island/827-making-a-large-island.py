class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j, new_color):
            if i<0 or i>=M or j<0 or j>=N or\
            visited[i][j] == new_color or grid[i][j] == 0:
                return
            
            visited[i][j] = new_color
            mp[new_color] = 1+mp.get(new_color, 0)
            
            dfs(i-1,j, new_color)
            dfs(i+1,j, new_color)
            dfs(i,j-1, new_color)
            dfs(i,j+1, new_color)
        
        M,N = len(grid), len(grid[0])
        
        visited = [[0 for _ in range(N)] for _ in range(M)]
        
        counter = 1
        mp = defaultdict()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    counter+=1
                    dfs(i,j, counter)
        
        if mp:
            res = max([v for k,v in mp.items()])
        else:
            res = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    st = set()

                    for dx, dy in directions:
                        if 0<=i+dx<M and 0<=j+dy<N:
                            if visited[i+dx][j+dy] != 0:
                                st.add(visited[i+dx][j+dy])
                        
                        count = 1
                        for ele in st:
                            count+=mp[ele]
                        
                        res = max(res, count)
                            
        return res
                    