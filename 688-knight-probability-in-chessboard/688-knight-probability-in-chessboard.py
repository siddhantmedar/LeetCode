class Solution:
    def knightProbability(self, N: int, k: int, r: int, c: int) -> float:
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

                            if 0<=x<N and 0<=y<N:
                                next[x][y] += curr[i][j]/8
                                
            curr = next

        return sum([sum(x) for x in curr])
        