class Solution:
    def numberOfSteps(self, num: int) -> int:
        def solve(n):
            if n == 0:
                return 0
            
            option1, option2 = float("inf"), float("inf")
            if n%2:
                option1 = 1 + solve(n-1)
            else:
                option2 = 1+solve(n//2)
                
            return min(option1, option2)
        
        return solve(num)