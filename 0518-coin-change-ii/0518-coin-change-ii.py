class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def solve(idx,rem):
            if rem == 0:
                return 1
            
            if idx>=len(coins) or rem < 0:
                return 0
            
            if dp[idx][rem] != -1:
                return dp[idx][rem]
            
            dp[idx][rem] = solve(idx+1,rem)+solve(idx,rem-coins[idx])
            
            return dp[idx][rem]
        
        
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        
        return solve(0,amount)