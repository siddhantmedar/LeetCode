class Solution:
    def climbStairs(self, n: int) -> int:
        def solve1(n):
            if n == 0 or n == 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]    
            
            dp[n] = solve(n-1) + solve(n-2)
            
            return dp[n]
        
        dp = [-1 for _ in range(n+1)]
        
        # return solve1(n)
        
        def solve2():
            prepre, pre = 1, 1
            
            for i in range(2, n+1):
                curr = pre + prepre
                
                prepre = pre
                pre = curr
            
            return pre
        
        return solve2()