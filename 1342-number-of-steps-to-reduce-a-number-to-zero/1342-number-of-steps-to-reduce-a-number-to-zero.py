class Solution:
    def numberOfSteps(self, num: int) -> int:
        def solve(n):
            count = 0
            
            while n != 0:
                if n%2:
                    n-=1
                else:
                    n//=2
                    
                count+=1
                
            return count
        
        return solve(num)