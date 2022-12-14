class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isSafe(row,col,x):
            for c in range(9):
                if c == col:
                    continue
                if board[row][c] == x:
                    return False
                
            for r in range(9):
                if r == row:
                    continue
                if board[r][col] == x:
                    return False
                    
            sx,sy = (row//3)*3,(col//3)*3
            
            for i in range(sx,sx+3):
                for j in range(sy,sy+3):
                    if (i,j) == (row,col):
                        continue
                        
                    if board[i][j] == x:
                        return False
                    
            return True
            
            
        def solve(row,col):
            if row == M:
                res = copy.deepcopy(board)
                return True
            
            if col == N:
                return solve(row+1,0)
            
            if board[row][col] != ".":
                return solve(row,col+1)
            
            for num in range(1,10):
                if isSafe(row,col,str(num)):
                    board[row][col] = str(num)
                    
                    if solve(row,col+1):
                        return True
                    
                    board[row][col] = "."
                    
            return False
            
            
        M,N = len(board),len(board[0])
        res = None
        return solve(0,0)