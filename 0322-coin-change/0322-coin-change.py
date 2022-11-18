class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(rem):
            if rem < 0:
                return -1
            
            if rem == 0:
                return 0
            
            result = float("inf")
            
            for coin in coins:
                sub = solve(rem-coin)
                
                if sub != -1:
                    result = min(result, sub+1)
                
            return result if result!=float("inf") else -1
        
        
        return solve(amount)