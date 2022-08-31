class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == word[0]:
                    q.append((i,j))
            
        st = list()
        visited = set()
        while q:
            i,j = q.popleft()
            st.append((i,j,0, False))
            
        while st:
            i, j, idx, backtrack = st.pop()
            
            if backtrack:
                visited.remove((i,j))
                continue
                
            visited.add((i,j))
            
            st.append((i,j, idx, True))
            
            if idx == len(word)-1:
                return True
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                if 0<=dx<M and 0<=dy<N and (dx,dy) not in visited\
                and grid[dx][dy] == word[idx+1]:
                    st.append((dx,dy, idx+1, False))
        
        return False