class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def solve(i,j):
            if i == 0:
                return j
            
            elif j == 0:
                return i
            
            val = 1
            
            if word1[i-1] == word2[j-1]:
                val = 0
                return solve(i-1,j-1) + val
            
            else:
                return min(solve(i,j-1),
                          solve(i-1,j-1),
                          solve(i-1,j)
                          ) + val
            
        return solve(len(word1), len(word2))