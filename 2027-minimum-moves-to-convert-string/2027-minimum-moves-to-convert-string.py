class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        
        s = list(s)
        
        for i in range(len(s)):
            if s[i] != "X":
                continue
            
            for x in (0,1,2):
                if i+x < len(s) and s[i+x]=="X":
                    s[i+x] = "O"
            
            cnt+=1
        
        return cnt
                   