class Solution:
    def getRow(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            nxt = [0]*(n+1)
            
            for j in range(len(dp)):
                if j==0:
                    nxt[j] = dp[j]
                    
                else:
                    first = dp[j-1]
                    second = dp[j]
                    
                    nxt[j] = first+second
            
            dp = nxt
                    
        return dp
        