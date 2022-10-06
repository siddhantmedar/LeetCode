class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(idx):
            if idx == len(s):
                return True
            
            if idx in dp:
                return dp[idx]
            
            for i in range(idx, len(s)):
                if s[idx:i+1] in wordDict and solve(i+1):
                    dp[idx] = True
                    return dp[idx]
                
            dp[idx] = False
            return dp[idx]
        
        
        dp = defaultdict()
        
        return solve(0)