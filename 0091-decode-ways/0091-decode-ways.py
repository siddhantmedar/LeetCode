class Solution:
    def numDecodings(self, s: str) -> int:
        def solve(idx):
            if idx < len(s) and s[idx] == "0":
                return 0
            
            if idx >= len(s)-1:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            cnt = solve(idx+1)
            
            if int(s[idx:idx+2]) <= 26:
                cnt+=solve(idx+2)
                
            dp[idx] = cnt

            return dp[idx]
        
        
        dp = [-1 for i in range(len(s)+1)]
        
        return solve(0)