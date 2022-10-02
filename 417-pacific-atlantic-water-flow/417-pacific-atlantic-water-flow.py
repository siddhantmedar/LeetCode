class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            def dfs(i, j, st, par):
                if i<0 or i>=m or j<0 or j>=n or par > heights[i][j] or (i,j) in st:
                    return
            
                st.add((i,j))

                for x,y in directions:
                    x = x+i
                    y = y+j

                    if (x,y) not in st:
                        dfs(x, y, st, heights[i][j])

            
            m,n = len(heights), len(heights[0])
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            pacific, atlantic = set(), set()

            for j in range(n):
                dfs(0,j,pacific,heights[0][j])
                dfs(m-1,j,atlantic,heights[m-1][j])

            for i in range(m):
                dfs(i,0,pacific,heights[i][0])
                dfs(i,n-1,atlantic,heights[i][n-1])

            return list(atlantic.intersection(pacific))