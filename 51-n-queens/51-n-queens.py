class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        def isSafe(i,j):
            row, col = i-1, j

            left, right = j-1, j+1

            while row >= 0:
                if board[row][col] == "Q" or (left >= 0 and board[row][left] == "Q")\
                or (right < N and board[row][right] == "Q"):
                    return False

                row-=1
                left-=1
                right+=1

            return True
        
        def NQueensRec(row):
            nonlocal result
            
            if row == N:
                result.append((["".join(row) for row in board]))
                return

            for col in range(N):
                if isSafe(row, col):
                    board[row][col] = "Q"

                    NQueensRec(row+1)

                    board[row][col] = "."
        
        board = [["." for _ in range(N)] for _ in range(N)]
        
        result = []
        
        NQueensRec(0)
        
        return result