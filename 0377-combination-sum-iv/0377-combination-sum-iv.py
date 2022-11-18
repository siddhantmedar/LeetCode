class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def solve(rem):
            if rem == 0:
                return 1
            
            if rem < 0:
                return 0
            
            if dp[rem] != -1:
                return dp[rem]
            ways = 0
            
            for ele in nums:
                ways+=solve(rem-ele)
                
            dp[rem] = ways
            
            return dp[rem]
        
        
        dp = [-1 for _ in range(target+1)]
        
        return solve(target)