class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        visited = set()
        M,N = len(grid), len(grid[0])
        
        if grid[0][0] == 0:
            visited.add((0,0))
            q = deque([(0,0)])
            depth = 0 
        
            while q:
                n = len(q)
                depth+=1
                for i in range(n):
                    i,j = q.popleft()

                    if i == M-1 and j == N-1:
                        return depth

                    for dx,dy in directions:
                        if 0<=i+dx<M and 0<=j+dy<N and (i+dx, j+dy) not in visited\
                        and grid[i+dx][j+dy] == 0:
                            visited.add((i+dx, j+dy))
                            q.append((i+dx,j+dy))
                        
        return -1