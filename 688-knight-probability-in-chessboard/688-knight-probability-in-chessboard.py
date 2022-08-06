class Solution:
    def knightProbability(self, N: int, k: int, r: int, c: int) -> float:
        def isValid(i,j):
            return 0<=i<N and 0<=j<N

        def printMat(x,y):
            for row in x:
                print(row, end='')
                print()

            print("\n")

            for row in y:
                print(row, end='')
                print()

        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

        curr = [[0 for _ in range(N)] for _ in range(N)]
        next = [[0 for _ in range(N)] for _ in range(N)]

        curr[r][c] = 1

        while k:
            next = [[0 for _ in range(N)] for _ in range(N)]

            for i in range(len(curr)):
                for j in range(len(curr[0])):
                    if curr[i][j]:

                        for x,y in directions:
                            x+=i
                            y+=j

                            if isValid(x,y):
                                next[x][y] += curr[i][j]/8
                                
            curr = next
            k-=1

        return sum([sum(x) for x in curr])
        