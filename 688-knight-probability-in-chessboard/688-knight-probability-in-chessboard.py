class Solution:
    def knightProbability(self, N: int, k: int, r: int, c: int) -> float:
        def isValid(i,j):
            return 0<=i<N and 0<=j<N

        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

        curr = [[0 for _ in range(N)] for _ in range(N)]
        next = [[0 for _ in range(N)] for _ in range(N)]

        curr[r][c] = 1

        for m in range(k):
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

        return sum([sum(x) for x in curr])
        