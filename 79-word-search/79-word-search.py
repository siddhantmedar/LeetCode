class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        # get starting points
        
        q = deque()
        
        M,N = len(grid), len(grid[0])
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == word[0]:
                    q.append((i,j))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        st = [(i,j, False, 0, grid[i][j]) for i,j in q]
        
        while st:
            i,j, backtrack, idx, w = st.pop()
            visited.add((i,j))
            
            if backtrack:
                visited.remove((i,j))
                continue
                
            if w == word:
                return True
            
            st.append((i,j, True, idx, w))
            
            if word[idx] != grid[i][j]:
                continue
                
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                if 0<=dx<M and 0<=dy<N and (dx, dy) not in visited:
                    st.append((dx,dy,False, idx+1, w+grid[dx][dy]))
                    
        return False