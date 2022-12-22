class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        def solve(idx):
            if idx > mx:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            if idx in days:
                dp[idx] = min(
                solve(idx+1)+cost[0],
                solve(idx+7)+cost[1],
                solve(idx+30)+cost[2]
                )
                return dp[idx]
            
            else:
                dp[idx] = solve(idx+1)
                return dp[idx]
            
        
        mx = max(days)
        days = set(days)
        
        dp = [-1 for _ in range(mx+1)]
        
        return solve(1)