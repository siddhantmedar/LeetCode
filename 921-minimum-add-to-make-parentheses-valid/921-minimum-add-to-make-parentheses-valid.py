class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0
        
        for c in s:
            if c == "(":
                balance+=1
                
            elif c == ")":
                balance-=1
                
            if balance == -1:
                ans+=1
                balance = 0
                
        return balance+ans