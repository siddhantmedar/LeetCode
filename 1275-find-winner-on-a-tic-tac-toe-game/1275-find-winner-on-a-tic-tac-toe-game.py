class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(turn):
            sym = "X" if turn==1 else "O"

            if all(box[0][c]==sym for c in range(3)):
                print("row 0")
                return True
            elif all(box[2][c]==sym for c in range(3)):
                print("row 2")
                return True
            elif all(box[r][0]==sym for r in range(3)):
                print("col 0")
                return True
            elif all(box[r][2]==sym for r in range(3)):
                print("col 2")
                return True
            elif all(box[i][i]==sym for i in range(3)):
                print("diag")
                return True
            elif all(box[1][c]==sym for c in range(3)):
                print("mid row")
                return True
            elif all(box[r][1]==sym for r in range(3)):
                print("mid col")
                return True
            
            i,j = 0,2
            valid = True
            
            while i<=2 and j>=0:
                if box[i][j] != sym:
                    valid = False
                i+=1
                j-=1
                
            if valid:
                print("rdiag")
                return True
            
            return False
        
        
        box = [[""]*3 for _ in range(3)]
        empty = 9
        
        def printBox():
            for r in box:
                print(r,end="\n")
        
        p1,p2 = False,False
        
        for i,(x,y) in enumerate(moves):
            if i%2==0:
                box[x][y]="X"
                # if check(1):
                #     printBox()
                #     return "A"
            else:
                box[x][y]="O"
                # if check(0):
                #     printBox()
                #     return "B"   
            empty-=1
        
        printBox()
        print("empty ",empty)
        
        if check(1):
            return "A"
        if check(0):
            return "B"
        
        return "Draw" if empty==0 else "Pending"