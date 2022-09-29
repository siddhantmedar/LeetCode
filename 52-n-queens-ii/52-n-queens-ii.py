class Solution:
    def totalNQueens(self, N: int) -> int:
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
            
            if row == N:
                return 1
            
            ways = 0
            for col in range(N):
                if isSafe(row, col):
                    board[row][col] = "Q"

                    ways+=NQueensRec(row+1)

                    board[row][col] = "."
            
            return ways 
        
        board = [["." for _ in range(N)] for _ in range(N)]
        
        return NQueensRec(0)