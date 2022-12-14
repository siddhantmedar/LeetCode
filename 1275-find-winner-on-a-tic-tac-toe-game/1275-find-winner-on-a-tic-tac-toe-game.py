class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(turn):
            sym = "X" if turn==1 else "O"

            if all(box[0][c]==sym for c in range(3)) or\
            all(box[2][c]==sym for c in range(3)) or\
            all(box[r][0]==sym for r in range(3)) or\
            all(box[r][2]==sym for r in range(3)) or\
            all(box[i][i]==sym for i in range(3)) or\
            all(box[1][c]==sym for c in range(3)) or\
            all(box[r][1]==sym for r in range(3)):
                return True
            
            i,j = 0,2
            valid = True
            
            while i<=2 and j>=0:
                if box[i][j] != sym:
                    valid = False
                i+=1
                j-=1
                
            return True if valid else False
        
        
        box = [[""]*3 for _ in range(3)]
        empty = 9

        for i,(x,y) in enumerate(moves):
            if i%2==0:
                box[x][y]="X"
            else:
                box[x][y]="O"  
            empty-=1
        
        if check(1):
            return "A"
        if check(0):
            return "B"
        
        return "Draw" if empty==0 else "Pending"