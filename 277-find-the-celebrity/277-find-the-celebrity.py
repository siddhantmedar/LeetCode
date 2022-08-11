# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def knowsMemo(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = knows(i,j)
            
            return dp[(i,j)]
        
        def confirm(i):
            for j in range(n):
                if j!=i:
                    if knowsMemo(i,j) or not knowsMemo(j,i):
                        return False
            
            return True
        
        dp = {}
        cand = 0
        
        for i in range(1,n):
            if knowsMemo(cand,i):
                cand = i
                
        return cand if confirm(cand) else -1       
            
        