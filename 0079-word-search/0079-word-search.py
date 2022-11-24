class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            
            if i<0 or i>=M or j<0 or j>=N or (i,j) in visited or board[i][j] != word[idx]:
                return False
            
            visited.add((i,j))
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                if dfs(dx,dy,idx+1):
                    return True
            
            visited.remove((i,j))
            return False
            
        
        M,N = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i,j,0):
                        return True
                    
                    
        return False
    