class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance, res = 0, 0
        
        for c in s:
            if c == "(":
                balance+=1
                
            elif c == ")":
                balance-=1
                
            if balance < 0:
                res+=1
                balance = 0
                
        return balance+res