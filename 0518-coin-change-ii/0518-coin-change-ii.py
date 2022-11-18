class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def solve(idx,rem):
            if rem == 0:
                return 1
            
            if idx>=len(coins) or rem < 0:
                return 0
            
            return solve(idx+1,rem)+solve(idx,rem-coins[idx])
        
        
        return solve(0,amount)