# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def confirm(i):
            for j in range(n):
                if j!=i:
                    if knows(i,j) or not knows(j,i):
                        return False
            return True
        
        
        cand = 0
        
        for i in range(1,n):
            if knows(cand,i):
                cand = i
        
        return cand if confirm(cand) else -1       
            
        