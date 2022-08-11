# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def confirm(i):
            for j in range(n):
                if j!=i:
                    if (i,j) in dp:
                        knows_else =  dp[(i,j)]
                    else:
                        knows_else = knows(i,j)
                        dp[(i,j)] = knows_else
                        
                    if (j,i) in dp:
                        known = dp[(j,i)]
                        
                    else:
                        known = knows(j,i)
                        dp[(j,i)] = known
                    
                    if knows_else or not known:
                        return False
            
            return True
        
        dp = {}
        cand = 0
        
        for i in range(1,n):
            result = knows(cand,i)
            if result:
                cand = i
            dp[(cand, i)] = result
            
        return cand if confirm(cand) else -1       
            
        