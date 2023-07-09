class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M,N = len(board), len(board[0])
        
        def dfs(i,j, idx):
            if idx == len(word):
                return True
            
            if i<0 or i>=M or j<0 or j>=N or (i,j) in visited or board[i][j] != word[idx]:
                return False
                
            visited.add((i,j))
            
            for dx,dy in dir:
                dx+=i
                dy+=j
                
                if dfs(dx,dy,idx+1):
                    return True
            
            visited.remove((i,j))
            
        
        visited = set()
        
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(M):
            for j in range(N):
                if word[0] == board[i][j]:
                    visited.clear()
                    if dfs(i,j,0):
                        return True
                    
        return False